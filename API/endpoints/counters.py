import requests

from API.endpoints.base_endpoint import Endpoint
from utilities.constants import API_HOST, API_PETITION


class Counters(Endpoint):

    def get_counters(self, headers_with_token):
        self.response = requests.get(f'{API_HOST}{API_PETITION}counters', headers=headers_with_token)
        self.response_json = self.response.json()

    def check_counters_keys(self):
        expected_keys = ['hidden_expected_keys']
        assert all(key in self.response_json for key in expected_keys)
