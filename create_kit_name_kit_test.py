import data as da
import sender_stand_request as se
import requests as re
import configuration as conf

#Funciones para crear kits.
auth_token = se.create_new_user(da.user_body, da.user_headers).json()["authToken"]
def crear_kit_sin_parametro(token):
    newk_head = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    newk_body = {

    }
    return re.post(conf.URL_SERVICE + conf.KITS_PATH, headers=newk_head, json=newk_body)

def crear_kit_nuevo(name, token):
    newk_head = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    newk_body = {
    "name" : name
              }
    return re.post(conf.URL_SERVICE + conf.KITS_PATH, headers= newk_head,json= newk_body)

def positive(caracter,token):
    response = crear_kit_nuevo(caracter, token)
    return response

#Pruebas
def test_numero_permitido_de_caracteres_2():
    response = positive("a",auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == "a"

def test_numero_permitido_de_caracteres_15():
    response = positive("El valor de prueba para esta comprobación será inferior a",auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == "El valor de prueba para esta comprobación será inferior a"


def test_numero_menor_de_caracteres():
    response = positive("",auth_token)
    assert response.status_code == 400

def test_el_número_de_caracteres_es_mayor_al_permitido():
    response = positive("El valor de prueba para esta comprobación será inferior a",auth_token)
    assert response.status_code == 400

def se_permiten_caracteres_especiales():
    response = positive("№%@\",")
    assert response.status_code == 201
    assert response.json["name"] == "№%@\","

def test_se_permiten_espacios():
    response = positive("A Aaa")
    assert response.status_code == 201
    assert response.json()["name"] == "A Aaa"

def test_se_permiten_numeros():
    response = positive("123")
    assert response.status_code == 201
    assert response.json()["name"] == "123"

def test_el_parametro_no_se_pasa_en_la_solicitud():
    response = crear_kit_sin_parametro(auth_token)
    assert response.status_code == 400

def test_se_pasa_un_tipo_de_parametro_diferente():
    response = crear_kit_nuevo(123,auth_token)
    assert response.status_code == 400

