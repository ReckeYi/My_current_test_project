import requests
from API.endpoints.base_endpoint import Endpoint
from utilities.constants import API_HOST, API_STATE, parent_state_id, state_id


class State(Endpoint):

    def state_create(self, headers_with_token, department_id, guest_petition_id):
        payload = {'hidden_payload'}
        self.response = requests.post(f"{API_HOST}{API_STATE}create", headers=headers_with_token,
                                      json=payload)
        self.response_json = self.response.json()

    def check_state_create_keys(self):
        assert "id" in self.response_json

    def get_state_list(self, headers_with_token, guest_petition_id):
        self.response = requests.get(
            f"{API_HOST}{API_STATE}list/{guest_petition_id}",
            headers=headers_with_token)
        self.response_json = self.response.json()

    def check_state_list_keys(self):
        expected_keys = ['hidden_expected_keys']
        assert isinstance(self.response_json, list)
        for item in self.response_json:
            assert all(key in item for key in expected_keys)

    def get_state_responsible(self, headers_with_token, guest_petition_id):
        self.response = requests.get(
            f"{API_HOST}{API_STATE}responsible/{guest_petition_id}",
            headers=headers_with_token
        )
        self.response_json = self.response.json()

    def check_state_responsible_keys(self):
        assert isinstance(self.response_json, list)
        assert len(self.response_json) == 1

        if self.response_json:
            responsible = self.response_json[0]
            expected_keys = ['hidden_expected_keys']
            assert all(key in responsible for key in expected_keys)

    def get_state(self, headers_with_token):
        self.response = requests.get(
            f"{API_HOST}{API_STATE}{state_id}",
            headers=headers_with_token
        )
        self.response_json = self.response.json()

    def check_state(self):
        expected_keys = ['hidden_expected_keys']
        assert isinstance(self.response_json, dict)
        assert all(key in self.response_json for key in expected_keys)
