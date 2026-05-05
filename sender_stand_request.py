import requests

import configuration
import data


def create_new_user(user_body, headers):
    """Crea un nuevo usuario y devuelve la respuesta de la API."""
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=user_body,
        headers=headers
    )


def post_new_kit(auth_token, kit_body):
    """Crea un nuevo kit usando el token de autorización del usuario."""
    headers = data.user_headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"

    return requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        json=kit_body,
        headers=headers
    )