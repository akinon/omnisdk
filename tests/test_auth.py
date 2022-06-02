from __future__ import unicode_literals

from .base import OmniSDKTestCase


class AuthTestCase(OmniSDKTestCase):
    def test_omnitron_successful_auth(self):
        self.omnisdk.omnitron_client(self.creds.url, self.creds.username, self.creds.password)

    def test_omnitron_unsuccessful_auth(self):
        with self.assertRaises(self.omnisdk.validation_error):
            self.omnisdk.omnitron_client(self.creds.url, "", "")

    def test_integration_successful_auth(self):
        self.omnisdk.integration_client(self.creds.url, self.creds.username, self.creds.password)

    def test_integration_unsuccessful_auth(self):
        with self.assertRaises(self.omnisdk.validation_error):
            self.omnisdk.integration_client(self.creds.url, "", "")

    def test_key_refreshed_automatically(self):
        pass
