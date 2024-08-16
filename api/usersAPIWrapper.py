import requests

class UsersAPIWrapper:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com/users"

    def listar_usuarios(self):
        response = requests.get(self.base_url)
        return response.json()

    def criar_usuario(self, user_data):
        response = requests.post(self.base_url, json=user_data)
        return response.json()

    def ler_usuario(self, user_id):
        response = requests.get(f"{self.base_url}/{user_id}")
        return response.json()

    def atualizar_usuario(self, user_id, user_data):
        response = requests.patch(f"{self.base_url}/{user_id}", json=user_data)
        return response.json()

    def deletar_usuario(self, user_id):
        response = requests.delete(f"{self.base_url}/{user_id}")
        return response.status_code

def exibir_menu():
    print(10 * '=' + ' MENU ' + 10 * '=')
    print('1 - Listar todos os usuários.')
    print('2 - Listar tarefas de um usuário específico.')
    print('3 - Operações CRUD em um usuário.')
    print(40 * '=')

def listar_tarefas_usuario():
    usuario_id = int(input('Digite o ID do usuário: '))
    print(10 * '=' + f' Tarefas do Usuário {usuario_id} ' + 10 * '=')
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{usuario_id}/todos')
    tarefas = response.json()
    for tarefa in tarefas:
        print(f"Tarefa: {tarefa['title']}")

def crud_usuario(api):
    print(10 * '=' + ' CRUD de Usuário ' + 10 * '=')
    print('1 - Criar Usuário')
    print('2 - Ler Usuário')
    print('3 - Atualizar Usuário')
    print('4 - Deletar Usuário')
    opcao_crud = int(input('Escolha uma opção: '))

    if opcao_crud == 1:
        username = input('Digite o username: ')
        novo_usuario = {
            "name": username,
            "username": username,
            "email": "exemplo@exemplo.com",
            "address": {
                "street": "Rua Exemplo",
                "suite": "Apt. 101",
                "city": "Cidade Exemplo",
                "zipcode": "00000-000"
            },
            "phone": "0000-0000",
            "website": "exemplo.com",
            "company": {
                "name": "Empresa Exemplo",
                "catchPhrase": "Frase de impacto",
                "bs": "slogan"
            }
        }
        response = api.criar_usuario(novo_usuario)
        print('')
        print(f"Usuário criado com sucesso! Status: {response}")
        print(f"Dados do Usuário: {response}")

    elif opcao_crud == 2:
        usuario_id = int(input('Digite o ID do usuário: '))
        response = api.ler_usuario(usuario_id)
        print(f"Dados do Usuário {usuario_id}: {response}")

    elif opcao_crud == 3:
        usuario_id = int(input('Digite o ID do usuário: '))
        novo_username = input('Digite o novo username: ')
        dados_atualizados = {"username": novo_username}
        response = api.atualizar_usuario(usuario_id, dados_atualizados)
        print(f"Usuário atualizado: {response}")

    elif opcao_crud == 4:
        usuario_id = int(input('Digite o ID do usuário: '))
        status_code = api.deletar_usuario(usuario_id)
        print(f"Usuário deletado com sucesso! Status: {status_code}")

def main():
    api = UsersAPIWrapper()
    exibir_menu()
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        usuarios = api.listar_usuarios()
        print(10 * '=' + ' Lista de Usuários ' + 10 * '=')
        for usuario in usuarios:
            print(f"{usuario['id']} - {usuario['username']}")
    elif opcao == 2:
        listar_tarefas_usuario()
    elif opcao == 3:
        crud_usuario(api)
    else:
        print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()
