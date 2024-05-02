import requests

from API.endpoints.base_endpoint import Endpoint
from utilities.constants import API_HOST, API_DEPARTMENTS


class Departments(Endpoint):
    id = None

    def get_departments(self):
        self.response = requests.get(f'{API_HOST}{API_DEPARTMENTS}')
        self.response_json = self.response.json()
        self.id = self.response_json[0]["id"]

    def check_departments_keys(self):
        expected_keys = ['hidden_expected_keys']
        for item in self.response_json:
            assert all(key in item for key in expected_keys)
