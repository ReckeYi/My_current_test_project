from API.endpoints.calendar import Calendar
from API.endpoints.counters import Counters
from API.endpoints.departments import Departments
from API.endpoints.guest import Guest
from API.endpoints.operator import Operator
from API.endpoints.receivers import Receivers
from API.endpoints.reception_user import ReceptionUser
from API.endpoints.state import State
from API.endpoints.topics import Topics
from API.endpoints.user import User
from API.endpoints.view import View


def test_update_calendar(headers_with_token):
    new_object_endpoint = Calendar()
    new_object_endpoint.update(headers_with_token)
    new_object_endpoint.check_status_true()
    new_object_endpoint.check_response_is_200()


def test_get_calendar_years(headers_with_token):
    new_object_endpoint = Calendar()
    new_object_endpoint.get_calendar_years(headers_with_token)
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_calendar_years_keys()


def test_calendar_year(headers_with_token):
    new_object_endpoint = Calendar()
    new_object_endpoint.get_calendar_year(headers_with_token)
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_calendar_year_keys()


def test_counters(headers_with_token):
    new_object_endpoint = Counters()
    new_object_endpoint.get_counters(headers_with_token)
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_counters_keys()


def test_petition_departments():
    new_object_endpoint = Departments()
    new_object_endpoint.get_departments()
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_departments_keys()


def test_petition_guest_create(department_id):
    new_object_endpoint = Guest()
    new_object_endpoint.guest_create(department_id)
    new_object_endpoint.check_response_is_201()
    new_object_endpoint.check_guest_create_keys()


def test_petition_guest_view(department_id):
    new_object_endpoint = Guest()
    new_object_endpoint.guest_create(department_id)
    new_object_endpoint.guest_view()
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_guest_view_keys()


def test_petition_operator_list(headers_with_token):
    new_object_endpoint = Operator()
    new_object_endpoint.get_operator_list(headers_with_token)
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_operator_list_keys()


def test_petition_operator_states(headers_with_token):
    new_object_endpoint = Operator()
    new_object_endpoint.get_operator_states(headers_with_token)
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_operator_states_keys()


def test_petition_receivers():
    new_object_endpoint = Receivers()
    new_object_endpoint.get_receivers()
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_receivers_keys()


def test_petition_state_create(headers_with_token, department_id, guest_petition_id):
    new_object_endpoint = State()
    new_object_endpoint.state_create(headers_with_token, department_id, guest_petition_id)
    new_object_endpoint.check_response_is_201()
    new_object_endpoint.check_state_create_keys()


def test_petition_state_list(headers_with_token, guest_petition_id):
    new_object_endpoint = State()
    new_object_endpoint.get_state_list(headers_with_token, guest_petition_id)
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_state_list_keys()


def test_petition_state_responsible(headers_with_token, guest_petition_id):
    new_object_endpoint = State()
    new_object_endpoint.get_state_responsible(headers_with_token, guest_petition_id)
    new_object_endpoint.check_state_responsible_keys()
    new_object_endpoint.check_response_is_200()


def test_petition_state(headers_with_token):
    new_object_endpoint = State()
    new_object_endpoint.get_state(headers_with_token)
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_state()


def test_petition_topics():
    new_object_endpoint = Topics()
    new_object_endpoint.get_topics()
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_topics()


def test_petition_topics_create(headers_with_token):
    new_object_endpoint = Topics()
    new_object_endpoint.topics_create(headers_with_token)
    new_object_endpoint.check_response_is_201()
    new_object_endpoint.check_topics_create()
    new_object_endpoint.topic_delete(headers_with_token)


def test_petition_topic_delete(headers_with_token):
    new_object_endpoint = Topics()
    new_object_endpoint.topics_create(headers_with_token)
    new_object_endpoint.topic_delete(headers_with_token)
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_topic_delete()


def test_petition_topic_edit(headers_with_token):
    new_object_endpoint = Topics()
    new_object_endpoint.topics_create(headers_with_token)
    new_object_endpoint.topic_edit(headers_with_token)
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_topic_edit()
    new_object_endpoint.topic_delete(headers_with_token)


def test_user_list(headers_with_token):
    new_object_endpoint = User()
    new_object_endpoint.get_user_list(headers_with_token)
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_user_list()


def test_petition_view(headers_with_token, guest_petition_id):
    new_object_endpoint = View()
    new_object_endpoint.get_view(headers_with_token, guest_petition_id)
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_view()


def test_reception_user(headers_with_token):
    new_object_endpoint = ReceptionUser()
    new_object_endpoint.get_reception_user(headers_with_token)
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_reception_user()


def test_reception_user_email(headers_with_token):
    new_object_endpoint = ReceptionUser()
    new_object_endpoint.update_reception_user_email(headers_with_token)
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_reception_user_email()
