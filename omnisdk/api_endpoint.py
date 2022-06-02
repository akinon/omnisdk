from __future__ import unicode_literals

import abc
import functools
import json
import logging
import time
from json import JSONDecodeError

import backoff
import requests

from .base_client import BaseClient
from .exceptions import ClientMissingParameterException, ClientBadUrlException
import re

logger = logging.getLogger(__name__)


def backoff_handler(details):
    logger.error(f"backoff_handler - {str(details)}")
    time.sleep(10)


def raise_for_status(f):
    @functools.wraps(f)
    @backoff.on_exception(
        backoff.constant,
        requests.exceptions.RequestException,
        max_tries=10,
        giveup=lambda e: getattr(e.response, "status_code", 500) < 499,
        on_backoff=backoff_handler,
        giveup_log_level=logging.DEBUG
    )
    def wrapper(self, *a, **kw):
        response = f(self, *a, **kw)
        if response.status_code == 401:
            key = self._api.refresh_key()  # We try to re-authenticate once, to refresh the token
            self._api.session.headers.update({"Authorization": key})
            response = f(self, *a, **kw)
        # If the initial credentials still has access, no longer should raise 401 for authentication
        try:
            response.raise_for_status()
        except requests.HTTPError as err:
            if response.content and response.status_code // 100 != 5:
                content = json.loads(response.content)
                err.args = (err.args, content)
            raise err
        if response.ok and response.text:
            response = response.json()
            if self._raw:
                return response
            return self.get_model_response(response)
        return {}

    return wrapper


class ApiEndpointMeta(type):
    methods = ["create", "retrieve", "update", "delete", "list", "_get_options"]

    def __new__(mcs, *args, **kwargs):
        # TODO we do not support py2, maybe change this to __init_subclass__ if any pros?
        cls = type(*args, **kwargs)
        for method in mcs.methods:
            setattr(cls, method, raise_for_status(getattr(cls, method)))
        return cls


class ApiEndpoint(object, metaclass=ApiEndpointMeta):
    _pattern = re.compile(r'{([^}]*)}')
    _path_params = {}

    class NoDefault(object):
        pass

    def __init__(self, api_class_name, endpoint, model, raw=False, path=None,
                 **kwargs):
        self._api = BaseClient.get_instance(api_class_name)
        self._model = model
        self._endpoint = self._api.base_url + endpoint + "/"
        self._raw = raw
        self._path = path
        self._path_params = kwargs
        # self._options = self._get_options()  # This will be used to create our rules for the api
        # So that we can validate the input before it reaches the api

    def __call__(self, path=NoDefault, *args, **kwargs):
        self._path = path if path != self.NoDefault else self._path
        self._path_params.update(kwargs)
        return self

    def create(self, item, **kwargs):
        if not self._raw and item:
            item = item.get_parameters()
        return self._request(action="post",
                             endpoint=self._endpoint,
                             data=item,
                             **kwargs)

    def retrieve(self, id, **kwargs):
        return self._request(action="get",
                             endpoint=self._endpoint + str(id) + '/',
                             **kwargs)

    def update(self, id, item, **kwargs):
        if not self._raw and item:
            item = item.get_parameters()
        return self._request(action="patch",
                             endpoint=self._endpoint + str(id) + '/',
                             data=item,
                             **kwargs)

    def delete(self, id, **kwargs):
        return self._request(action="delete",
                             endpoint=self._endpoint + str(id) + '/',
                             **kwargs)

    def list(self, **kwargs):
        self.iterator = self._List(self)
        return self.iterator(**kwargs)

    def _list(self, **kwargs):
        return self._request(action="get",
                             endpoint=self._endpoint,
                             **kwargs)

    def _request(self, action, endpoint, *args, **kwargs):
        endpoint = self._get_endpoint_path(endpoint)
        if action in ["post", "patch", "put"]:
            return self._write_request(action, endpoint, *args, **kwargs)
        response = getattr(self._api.session, action)(endpoint, *args, **kwargs)
        return response

    def _write_request(self, action, endpoint, *args, **kwargs):
        headers = kwargs.pop("headers", {})
        headers["Content-Type"] = "application/json"
        data = kwargs.pop("data", {})
        response = getattr(self._api.session, action)(endpoint,
                                                      data=json.dumps(data),
                                                      headers=headers,
                                                      *args,
                                                      **kwargs
                                                      )
        return response

    def _get_endpoint_path(self, endpoint):
        """
        self._path name of a detail route if given
        self._path_params {"channel_id": 6}
        self._endpoint   localhost:8000/api/v1/channel/{channel_id}/products/
        :return:
        """
        if self._path:
            endpoint += self._path
            if not endpoint.endswith("/"):
                endpoint += "/"
        if "{" not in endpoint:
            return endpoint

        matched_keys = self._pattern.findall(endpoint)
        if not matched_keys:
            raise ClientBadUrlException
        matched_pairs = {}
        for key in matched_keys:
            if key not in self._path_params:
                raise ClientMissingParameterException(key)
            matched_pairs[key] = self._path_params.get(key)
        return endpoint.format(**matched_pairs)

    def _get_options(self):
        # TODO use options to get which parameters endpoint wants and send only those

        # TODO cache options response so that if we want to send n request to omnitron
        #  for a model n+1 request suffices instead of sending options for each request
        #  making the total count 2n
        return self._api.session.options(self._endpoint)

    def get_model_response(self, response):
        if isinstance(response, list):
            items = []
            for entry in response:
                item = self._create_item(entry)
                items.append(item)
            return items
        elif "results" in response and isinstance(response["results"], list):
            items = []
            for entry in response["results"]:
                item = self._create_item(entry)
                items.append(item)
            return items
        return self._create_item(response)

    def _create_item(self, entry):
        item = self._model()
        for key, value in entry.items():
            setattr(item, key, value)
        return item

    class _Base(metaclass=abc.ABCMeta):
        def json(self):
            return self

    class _List(_Base):
        # Various list endpoint caching, paginating, meta-data about the endpoint will be done here.
        # The other CRUDL endpoint do not yet have these _METHOD classes implemented because I can't foresee the
        # relevant metadata we may need for those endpoint
        # But for this endpoint, we definitely
        def __init__(self, api_endpoint):
            self._api_endpoint = api_endpoint
            self._next = True
            self._page = 0

        def __call__(self, *args, **kwargs):
            params = kwargs.get("params", {})
            if "page" not in params:
                params["page"] = 1

            kwargs["params"] = params
            self._args = args
            self._kwargs = kwargs

            response = self._api_endpoint._list(*self._args, **self._kwargs)
            json_response = response.ok and response.json()
            if not json_response:
                return response
            if isinstance(json_response, list):
                self._next = False
            else:
                self._next = bool(json_response.get("next", True))
                params["page"] += 1
            return response

        def __iter__(self):
            return self

        def __next__(self):
            if not self._next:
                raise StopIteration
            params = self._kwargs.pop("params", {})
            self._kwargs["params"] = params
            response = self._api_endpoint._list(*self._args, **self._kwargs)
            return self.get_list(response)

        def get_list(self, response):
            response = response.ok and response.json()
            if isinstance(response, list):
                self._next = False
                return response
            self._next = bool(response.get("next", True))
            self._kwargs["params"]["page"] += 1
            if self._api_endpoint._raw:
                return response
            return self._api_endpoint.get_model_response(response)  # noqa
