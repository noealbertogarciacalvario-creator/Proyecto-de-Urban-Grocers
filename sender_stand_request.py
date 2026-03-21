import requests as re
import configuration as conf
import copy as c
import data as da



def create_new_user(body, header):
    return re.post(conf.URL_SERVICE + conf.CREATE_USER_PATH, json=body, headers=header)
def post_new_kit(auth_token,kit_body):
    headers = da.user_headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    return re.post(conf.URL_SERVICE + conf.KITS_PATH, json=kit_body, headers=headers)
