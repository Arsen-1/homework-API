#from qa_internship_api.conftest import env
#from conftest import env
#from conftest import fixture


class Config:
    def __init__(self, env):

        self.base_url = {
            "local": "https://localhost"
           # 'fakerest':'https://fakerestapi.azurewebsites.net'
        }[env]

        self.app_port = {
            'local': '80'
        }