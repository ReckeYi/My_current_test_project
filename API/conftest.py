import pytest

from utilities.connectors import token, new_department_id, new_guest_petition_id


@pytest.fixture
def headers_with_token():
    headers_with_token = {'Authorization': f'Bearer {token}'}
    return headers_with_token


@pytest.fixture
def department_id():
    department_id = new_department_id
    return department_id


@pytest.fixture
def guest_petition_id():
    guest_petition_id = new_guest_petition_id
    return guest_petition_id
