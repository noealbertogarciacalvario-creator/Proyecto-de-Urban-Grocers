import pytest

import api_client
import test_data


@pytest.fixture(scope="module")
def auth_token():
    response = api_client.create_new_user(
        data.kit_body,
        data.user_headers
    )

    assert response.status_code == 201, f"Error creando usuario: {response.text}"

    json_response = response.json()

    assert "authToken" in json_response, "No se recibió authToken en la respuesta"

    return json_response["authToken"]


def get_kit_body(name):
    kit_body = data.kit_body.copy()
    kit_body["name"] = name
    return kit_body


def assert_positive_response(auth_token, name):
    kit_body = get_kit_body(name)
    response = api_client.post_new_kit(auth_token, kit_body)

    assert response.status_code == 201
    assert response.json()["name"] == name


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
        get_kit_body(""),
        get_kit_body("a" * 512),
        {},
        get_kit_body(123),
    ]
)
def test_create_kit_with_invalid_name(auth_token, kit_body):
    assert_negative_response(auth_token, kit_body)

#Pruebas
def test_numero_permitido_de_caracteres():
    positive_assert("a")

def test_numero_permitido_de_caracteres_511():
    positive_assert("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopq")

def test_numero_menor_de_caracteres():
    negative_assert("")

def test_numero_mayor_permitido_de_caracteres_512():
    negative_assert("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqr")

def test_se_permiten_caracteres_especiales():
    positive_assert("№%@\",")

def test_se_permiten_espacios():
    positive_assert("A Aaa")

def test_se_permiten_numeros():
    positive_assert("123")

def test_el_parametro_no_se_pasa_en_la_solicitud():
    negative_assert()

def test_se_pasa_un_tipo_de_parametro_diferente():
    negative_assert(123)

