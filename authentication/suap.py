import requests
import getpass import getpass
import json



api_utl = "https://suap.ifrn.edu.br/api"

def autenticar(api_url):
    user = input ("user:")
    password = getpass()

    data= {"username": user , "password": password}
    response = requests.post(api_url+"v2/autenticacao/token",json=data)
    return






















    def main():
        api_url = "https://suap.ifrn.edu.br/api"


        with open('suap_keys.json', 'w+') as file:
            try:
                data=json.load(file)
            except json.decoder.JSONDecodeError:
                data = {}
                data['token'] = autenticar(api_url)
                json.dump(data,file)
token = data['token']
headers = {
    'Autorizatio':f'Bearer {token}'

}