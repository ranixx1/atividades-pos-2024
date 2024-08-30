import requests
from requests.auth import HTTPBasicAuth

def follow_user(user, token, username):
    """Seguir um usuário no GitHub."""
    try:
        response = requests.put(f"https://api.github.com/user/following/{username}", auth=HTTPBasicAuth(user, token))
        if response.status_code == 204:
            print(f'\nUsuário {username} foi seguido com sucesso!')
        else:
            print(f'\nErro ao seguir {username}. Código de status: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'\nOcorreu um erro ao tentar seguir o usuário: {e}')

def unfollow_user(user, token):
    """Deixar de seguir um usuário no GitHub."""
    try:
        followers = requests.get('https://api.github.com/user/following', auth=HTTPBasicAuth(user, token))
        if followers.status_code == 200:
            print('\nPessoas que você segue:')
            for follower in followers.json():
                print(f"{follower['login']}")
            print('')
            username = input('Digite o nome do usuário que vai deixar de seguir (username): ')
            response = requests.delete(f"https://api.github.com/user/following/{username}", auth=HTTPBasicAuth(user, token))
            if response.status_code == 204:
                print(f'\nVocê deixou de seguir {username} com sucesso!')
            else:
                print(f'\nErro ao deixar de seguir {username}. Código de status: {response.status_code}')
        else:
            print(f'\nErro ao obter a lista de seguidores. Código de status: {followers.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'\nOcorreu um erro ao tentar deixar de seguir o usuário: {e}')

def list_followers(user, token):
    """Listar seguidores do usuário no GitHub."""
    try:
        followers = requests.get('https://api.github.com/user/followers', auth=HTTPBasicAuth(user, token))
        if followers.status_code == 200:
            print('\nSeus seguidores:')
            for index, follower in enumerate(followers.json(), start=1):
                print(f"{index} - {follower['login']}")
        else:
            print(f'\nErro ao listar seguidores. Código de status: {followers.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'\nOcorreu um erro ao tentar listar os seguidores: {e}')

def main():
    """Função principal para executar o menu de opções."""
    user = input('Digite o usuário: ').strip()
    token = input('Digite o token: ').strip()
    print('')

    print(5*'=-' + ' MENU ' + '-='*5)
    print('1 - Seguir usuário.')
    print('2 - Deixar de seguir um usuário.')
    print('3 - Listar seus seguidores.')
    print('-='*13)

    choice = input('\nDigite a opção escolhida: ').strip()
    print('-='*13)

    if choice == '1':
        username = input('\nDigite o nome do usuário que deseja seguir (username): ').strip()
        follow_user(user, token, username)
    elif choice == '2':
        unfollow_user(user, token)
    elif choice == '3':
        list_followers(user, token)
    else:
        print('\nOpção inválida!')

if __name__ == "__main__":
    main()
