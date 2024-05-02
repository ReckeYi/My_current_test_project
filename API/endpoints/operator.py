import requests
from API.endpoints.base_endpoint import Endpoint
from utilities.constants import API_HOST, API_OPERATOR


class Operator(Endpoint):

    def get_operator_list(self, headers_with_token):
        self.response = requests.get(f'{API_HOST}{API_OPERATOR}list', headers=headers_with_token)
        self.response_json = self.response.json()

    def check_operator_list_keys(self):
        expected_keys = ['hidden_expected_keys']
        assert isinstance(self.response_json, dict)
        assert "total" in self.response_json
        assert "list" in self.response_json
        for item in self.response_json["list"]:
            assert all(key in item for key in expected_keys)

    def get_operator_states(self, headers_with_token):
        self.response = requests.get(f'{API_HOST}{API_OPERATOR}states', headers=headers_with_token)
        self.response_json = self.response.json()

    def check_operator_states_keys(self):
        assert isinstance(self.response_json, list)
        for item in self.response_json:
            assert 'id' in item
            assert 'name' in item
