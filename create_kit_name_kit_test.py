import data as da
import sender_stand_request as se
import requests as re
import configuration as conf

#Funciones para pruebas

auth_token = se.create_new_user(da.kit_body, da.user_headers).json()["authToken"]

def get_kit_body_empty():
    kit_body = da.kit_body_empty.copy()
    return kit_body

def get_kit_body(name):
    kit_body = da.kit_body.copy()
    kit_body["name"] = name
    return kit_body

def positive_assert(name):
    kit_body = get_kit_body(name)
    response = se.post_new_kit(auth_token,kit_body)
    assert response.status_code == 201
    assert response.json()["name"] == name

def negative_assert(name=None):
    if name is None:
        kit_body = get_kit_body_empty()
        response = se.post_new_kit(auth_token,kit_body)
        assert response.status_code == 400
    else:
        kit_body = get_kit_body(name)
        response = se.post_new_kit(auth_token,kit_body)
        assert response.status_code == 400


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

