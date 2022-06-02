import os
import textwrap
from unittest import TestCase

from requests import HTTPError

from omnisdk.omnitron.client import OmnitronApiClient
from omnisdk.exceptions import ValidationError


class OmniSDKTestCase(TestCase):
    # No need to import anything from omnisdk anymore, we have all the test-ables and test-ees here.
    # Below two class are just basic attributes dumps for ease of access and to not to pollute the test case's namespace
    class omnisdk(object):
        omnitron_client = OmnitronApiClient
        validation_error = ValidationError
        api_error = HTTPError

    class creds(object):
        url = os.environ.get("OMNITRON_URL")
        username = os.environ.get("OMNITRON_USERNAME")
        password = os.environ.get("OMNITRON_PASSWORD")

        if not all((url, username, password)):
            raise Exception(
                textwrap.dedent(
                    """

                    The tests of this library depends on the actual api, current setup for tests requires you to have
                    three environment variables available at the time of running the tests. Without these environment
                    variables, tests will refuse to run.

                    - OMNITRON_URL: omnitron base url to test against
                    - OMNITRON_USERNAME: a valid username for the api
                    - OMNITRON_PASSWORD: a valid password for the api for the OMNITRON_USERNAME
                    """
                )
            )
