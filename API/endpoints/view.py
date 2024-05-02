import requests
from API.endpoints.base_endpoint import Endpoint
from utilities.constants import API_HOST, API_PETITION


class View(Endpoint):

    def get_view(self, headers_with_token, guest_petition_id):
        self.response = requests.get(
            f'{API_HOST}{API_PETITION}view/{guest_petition_id}',
            headers=headers_with_token
        )
        self.response_json = self.response.json()

    def check_view(self):
        expected_keys = ['hidden_expected_keys']
        assert isinstance(self.response_json, dict)
        assert all(key in self.response_json for key in expected_keys)
