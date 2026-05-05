import requests

import configuration
import test_data


BASE_URL = configuration.URL_SERVICE


def create_new_user(body, headers):
    return requests.post(
        url=f"{BASE_URL}{configuration.CREATE_USER_PATH}",
        json=body,
        headers=headers
    )


def post_new_kit(auth_token, kit_body):
    headers = data.user_headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"

    return requests.post(
        url=f"{BASE_URL}{configuration.KITS_PATH}",
        json=kit_body,
        headers=headers
    )