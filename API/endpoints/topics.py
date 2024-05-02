import requests
from API.endpoints.base_endpoint import Endpoint
from utilities.constants import API_HOST, API_TOPICS
from utilities.utilites import RandomVariables


class Topics(Endpoint, RandomVariables):
    topic_id = None

    def get_topics(self):
        self.response = requests.get(f'{API_HOST}{API_TOPICS}')
        self.response_json = self.response.json()

    def check_topics(self):
        assert isinstance(self.response_json, list)
        for item in self.response_json:
            assert 'id' in item
            assert 'name' in item

    def topics_create(self, headers_with_token):
        payload = {'hidden_payload'}
        self.response = requests.post(f'{API_HOST}{API_TOPICS}create', headers=headers_with_token, json=payload)
        self.response_json = self.response.json()
        self.topic_id = self.response_json["id"]

    def check_topics_create(self):
        assert isinstance(self.response_json, dict)
        assert "id" in self.response_json

    def topic_delete(self, headers_with_token):
        payload = {'hidden_payload'}
        self.response = requests.patch(
            f'{API_HOST}{API_TOPICS}delete/{self.topic_id}',
            headers=headers_with_token, json=payload
        )
        self.response_json = self.response.json()

    def check_topic_delete(self):
        assert isinstance(self.response_json, dict)
        assert "status" in self.response_json
        assert self.response_json["status"] == True

    def topic_edit(self, headers_with_token):
        payload = {'hidden_payload'}
        self.response = requests.put(
            f'{API_HOST}{API_TOPICS}edit/{self.topic_id}',
            headers=headers_with_token, json=payload
        )
        self.response_json = self.response.json()

    def check_topic_edit(self):
        assert isinstance(self.response_json, dict)
        assert "status" in self.response_json
        assert self.response_json["status"] == True
