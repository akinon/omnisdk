from __future__ import unicode_literals

import abc
import weakref

import requests

from .exceptions import ValidationError, ClientNotInitializedException


class BaseClient(object, metaclass=abc.ABCMeta):
    client_route = ""
    instance = {}

    def __init__(self, base_url, username, password):
        self.session = requests.Session()

        # credentials
        self.base_url = base_url + self.client_route
        self.username = username
        self.password = password
        key = self.refresh_key()
        self.session.headers.update({"Authorization": key})

        BaseClient.instance[self.__class__.__name__] = weakref.proxy(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__class__.instance = None
        self.session.close()

    @staticmethod
    def get_instance(class_name):
        if BaseClient.instance.get(class_name):
            api = BaseClient.instance[class_name]
        else:
            raise ClientNotInitializedException
        return api

    def refresh_key(self):
        response = self.session.post(
            self.base_url + "auth/login/", json=dict(username=self.username, password=self.password)
        )
        # TODO fix non 400 html responses raises exception
        if response.status_code == 400:  # Most likely authentication error
            # We probably should allow the end user to decide on the action with a sane default
            # instead of blindly raising. This may cause inline declarations or context processors to
            # halt the process instead of
            json = response.json()
            raise ValidationError(str(json), json=json)
        return "Token {}".format(response.json()["key"])
