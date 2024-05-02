import requests

from utilities.constants import API_HOST, API_CALENDAR, year
from API.endpoints.base_endpoint import Endpoint
from utilities.utilites import RandomVariables


class Calendar(Endpoint, RandomVariables):
    def update(self, headers_with_token):
        payload = {'hidden_payload'}

        self.response = requests.put(f'{API_HOST}{API_CALENDAR}', headers=headers_with_token, json=payload)
        self.response_json = self.response.json()

    def check_status_true(self):
        assert self.response_json["status"] == True

    def get_calendar_years(self, headers_with_token):
        payload = {'hidden_payload'}
        self.response = requests.get(f'{API_HOST}{API_CALENDAR}years', headers=headers_with_token, json=payload)
        self.response_json = self.response.json()

    def check_calendar_years_keys(self):
        expected_keys = ['hidden_expected_keys']
        assert all(key in self.response_json for key in expected_keys)

    def get_calendar_year(self, headers_with_token):
        self.response = requests.get(f'{API_HOST}{API_CALENDAR}{year}', headers=headers_with_token)
        self.response_json = self.response.json()

    def check_calendar_year_keys(self):
        expected_keys = ['hidden_expected_keys']
        for item in self.response_json:
            assert all(key in item for key in expected_keys)
