import pytest

import api_client
import test_data as td


@pytest.fixture(scope="module")
def auth_token():
    response = api_client.create_new_user(
        td.VALID_USER_BODY,
        td.USER_HEADERS
    )

    assert response.status_code == 201, f"Error creando usuario: {response.text}"

    json_response = response.json()

    assert "authToken" in json_response, "No se recibió authToken en la respuesta"

    return json_response["authToken"]


def assert_positive_response(auth_token, name):
    kit_body = td.get_kit_body(name)

    response = api_client.post_new_kit(auth_token, kit_body)

    assert response.status_code == 201

    response_data = response.json()

    assert "name" in response_data
    assert response_data["name"] == name


def assert_negative_response(auth_token, kit_body):
    response = api_client.post_new_kit(auth_token, kit_body)

    assert response.status_code == 400


@pytest.mark.parametrize(
    "name",
    [
        "a",
        "a" * 511,
        "№%@\",",
        "A Aaa",
        "123",
    ]
)
def test_create_kit_with_valid_name(auth_token, name):
    assert_positive_response(auth_token, name)


@pytest.mark.parametrize(
    "kit_body",
    [
        td.get_kit_body(""),
        td.get_kit_body("a" * 512),
        {},
        td.get_kit_body(123),
    ]
)
def test_create_kit_with_invalid_name(auth_token, kit_body):
    assert_negative_response(auth_token, kit_body)