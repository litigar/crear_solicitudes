import base64
import os
import requests
from dotenv import load_dotenv

from liti_log import UtilLog


class admin_user(object):
    __instance = None

    def __str__(self):
        return 'admin_user Singleton file_name {} '.format(len(self.file_name))

    def __new__(cls):
        if not admin_user.__instance:
            admin_user.__instance = object.__new__(cls)
        return admin_user.__instance

    @staticmethod
    def get_instance():
        if not admin_user.__instance:
            admin_user.__instance = admin_user()
        return admin_user.__instance

    def __init__(self):
        self.url = os.environ.get('url')
        self.username = os.environ.get('user_name')
        self.password = os.environ.get('password')
        self.usr_dicc = {
            'username': self.username,
            'password': self.password
        }
        self.token = ""
        print(f"url {self.url}")

    def autentication(self) -> str:
        endpoint = self.url + 'login/'
        # print(f'autentication username ({self.username})')
        # print(f'autentication password ({self.password})')
        # reponse=requests.post(endpoint, auth=(self.username,self.password))
        payload = self.usr_dicc
        reponse = requests.post(endpoint, json=payload)
        print(f'autentication reponse.status_code {reponse.status_code}')
        # print(f'autentication despues json({reponse.json})')
        # print(f'autentication despues text({reponse.text})')
        if reponse.status_code == 200 or reponse.status_code == 201:
            reponse_json = reponse.json()
            # print(f"get_token json {reponse_json}")
            # print(f"autentication token {reponse_json['token']}")
            self.token = reponse_json['token']

    def get_token(self):
        endpoint = self.url + 'refresh-token/'
        headers = {'Content-Type': 'application/json'}
        # ,params={'username',self.username}
        reponse = requests.get(endpoint, headers=headers, params={'username': self.username})
        print(f'admin get_token reponse.status_code {reponse.status_code}')
        # print(f'get_token reponse {reponse}')
        # reponse_text = reponse.text
        # print(f"get_token json {reponse_text}")

        reponse_json = reponse.json()
        # print(f"get_token json {reponse_json}")

        if reponse.status_code == 200:
            # print(f"get_token token {reponse_json['token']}")
            self.token = reponse_json['token']
            return self.token
        else:
            UtilLog.get_instance().write(f"admin get_token reponse_json {reponse_json}")

        if reponse_json['expired']:
            self.autentication()
            return self.token
        UtilLog.get_instance().write(reponse_json['error'])

    def get_secuencia(self, secuencia):
        endpoint = self.url + 'secuencia/'
        token = 'Token ' + self.get_token()

        headers = {'Content-Type': 'application/json; charset=UTF-8', 'Authorization': token}
        # reponse=requests.get(endpoint, params={'pk':2})
        # print(f"get_secuencia radicacion_id {radicacion_id}")
        reponse = requests.get(endpoint, headers=headers, params={'secuencia': secuencia})
        # print(f'get_secuencia reponse.status_code {reponse.status_code}')
        # print(reponse)
        # print(reponse.url)
        json_item = reponse.json()
        # print(f"get_secuencia list_json {json_item}")

        if reponse.status_code == 200:
            # UtilLog.get_instance().write(f"get_secuencia secuencia {str(json_item['secuencia'])}")
            # UtilLog.get_instance().write(f"get_secuencia type {type(json_item['secuencia'])}")
            # UtilLog.get_instance().write(f"get_secuencia solicitud_id {radicacion_id} {json_item}")
            if json_item['estado'] == 'ok':
                return json_item['secuencia']
            else:
                UtilLog.get_instance().write(f"get_secuencia {json_item}")
        else:
            UtilLog.get_instance().write(f"get_secuencia json_item {json_item}")
        return 0
