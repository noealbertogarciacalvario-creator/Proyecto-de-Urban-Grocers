import requests as re
import configuration as conf



def create_new_user(body, header):
    return re.post(conf.URL_SERVICE + conf.CREATE_USER_PATH, json=body, headers=header)
def post_new_kit(authtoken):
    return re.post(conf.URL_SERVICE + conf.KITS_PATH, headers=authtoken)
