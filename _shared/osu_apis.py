import json
import os

from ossapi import Ossapi

error_message_apikey_not_set = \
    'Please fill apikeys in /RDC2024-tools/_shared/config.json\n' \
    'You can find keys in https://osu.ppy.sh/home/account/edit\n' \
    'format should be: \n' \
    '"osu_auth": \{"client_id": "{","client_secret": ""}'

def read_apikeys():
    client_id = None
    client_secret = None
    config_path = os.path.join(os.getcwd(), ".." , "_shared/config.json")
    with open(config_path) as f:
        data = json.load(f)
        try:
            client_id = data['osu_auth']['client_id']
            client_secret = data['osu_auth']['client_secret']
        except KeyError:
            return None
    return client_id,client_secret

def get_osu_api():
    client_id, client_secret = read_apikeys()
    error_flag = 0
    if (client_id is None) or (len(client_id) == 0):
        error_flag = error_flag | 1
    if (client_secret is None) or (len(client_secret) == 0):
        error_flag = error_flag | 1

    if (error_flag & 1 > 0):
        raise Exception(error_message_apikey_not_set)
    else:
        return Ossapi(client_id, client_secret)