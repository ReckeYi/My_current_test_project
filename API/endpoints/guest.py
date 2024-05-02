import requests
from API.endpoints.base_endpoint import Endpoint
from utilities.connectors import new_topic_id

from utilities.constants import API_HOST, API_GUEST, file_name
from utilities.utilites import RandomVariables


class Guest(Endpoint, RandomVariables):
    hash = None
    id = None

    def guest_create(self, department_id):
        payload = {'hidden_payload'}
        self.response = requests.post(f'{API_HOST}{API_GUEST}create', json=payload)
        self.response_json = self.response.json()
        self.hash = self.response_json['hash']
        self.id = self.response_json['id']

    def check_guest_create_keys(self):
        expected_keys = ['hidden_expected_keys']
        assert all(key in self.response_json for key in expected_keys)

    def guest_view(self):
        self.response = requests.get(f'{API_HOST}{API_GUEST}view/{self.hash}')
        self.response_json = self.response.json()

    def check_guest_view_keys(self):
        expected_keys = ['hidden_expected_keys']
        for key in expected_keys:
            assert key in self.response_json
