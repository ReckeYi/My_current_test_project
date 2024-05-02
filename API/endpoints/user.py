import requests
from API.endpoints.base_endpoint import Endpoint
from utilities.constants import API_HOST, API_PETITION


class User(Endpoint):

    def get_user_list(self, headers_with_token):
        self.response = requests.get(f'{API_HOST}{API_PETITION}user/list', headers=headers_with_token)
        self.response_json = self.response.json()

    def check_user_list(self):
        expected_keys = ['hidden_expected_keys']
        assert isinstance(self.response_json, dict)
        assert 'total' in self.response_json
        assert 'list' in self.response_json

        for item in self.response_json['list']:
            assert isinstance(item, dict)
            assert all(key in item for key in expected_keys)
