import requests
from API.endpoints.base_endpoint import Endpoint
from utilities.connectors import get_reception_user_id
from utilities.constants import API_HOST, API_RECEPTION_USER, user_email


class ReceptionUser(Endpoint):

    def get_reception_user(self, headers_with_token):
        self.response = requests.get(f'{API_HOST}{API_RECEPTION_USER}', headers=headers_with_token)
        self.response_json = self.response.json()

    def check_reception_user(self):
        expected_keys = ['hidden_expected_keys']
        assert isinstance(self.response_json, dict)
        assert all(key in self.response_json for key in expected_keys)

    def update_reception_user_email(self, headers_with_token):
        current_token = headers_with_token['Authorization'].split(' ')[1]
        payload = {'hidden_payload'}
        self.response = requests.patch(
            f'{API_HOST}{API_RECEPTION_USER}email',
            headers=headers_with_token,
            json=payload
        )
        self.response_json = self.response.json()

    def check_reception_user_email(self):
        assert 'status' in self.response_json
