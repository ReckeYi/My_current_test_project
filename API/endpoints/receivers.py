import requests
from API.endpoints.base_endpoint import Endpoint
from utilities.constants import API_HOST, API_PETITION


class Receivers(Endpoint):

    def get_receivers(self):
        self.response = requests.get(f'{API_HOST}{API_PETITION}receivers')
        self.response_json = self.response.json()

    def check_receivers_keys(self):
        expected_keys = ['hidden_expected_keys']
        assert isinstance(self.response_json, list)
        assert all(key in item for item in self.response_json for key in expected_keys)
