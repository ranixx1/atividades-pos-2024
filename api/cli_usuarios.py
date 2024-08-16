import requests

def exibir_menu():
    print(10 * '=' + ' MENU ' + 10 * '=')
    print('1 - Listar todos os usuários.')
    print('2 - Listar tarefas de um usuário específico.')
    print('3 - Operações CRUD em um usuário.')
    print(40 * '=')

def listar_usuarios():
    print(10 * '=' + ' Lista de Usuários ' + 10 * '=')
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    usuarios = response.json()
    for usuario in usuarios:
        print(f"{usuario['id']} - {usuario['username']}")

def listar_tarefas_usuario():
    usuario_id = int(input('Digite o ID do usuário: '))
    print(10 * '=' + f' Tarefas do Usuário {usuario_id} ' + 10 * '=')
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{usuario_id}/todos')
    tarefas = response.json()
    for tarefa in tarefas:
        print(f"Tarefa: {tarefa['title']}")

def crud_usuario():
    print(10 * '=' + ' CRUD de Usuário ' + 10 * '=')
    print('1 - Criar Usuário')
    print('2 - Ler Usuário')
    print('3 - Atualizar Usuário')
    print('4 - Deletar Usuário')
    opcao_crud = int(input('Escolha uma opção: '))

    if opcao_crud == 1:
        criar_usuario()
    elif opcao_crud == 2:
        ler_usuario()
    elif opcao_crud == 3:
        atualizar_usuario()
    elif opcao_crud == 4:
        deletar_usuario()

def criar_usuario():
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
    response = requests.post('https://jsonplaceholder.typicode.com/users', json=novo_usuario)
    print(f"Usuário criado com sucesso! Status: {response.status_code}")
    print(f"Dados do Usuário: {response.json()}")

def ler_usuario():
    usuario_id = int(input('Digite o ID do usuário: '))
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{usuario_id}')
    print(f"Dados do Usuário {usuario_id}: {response.json()}")

def atualizar_usuario():
    usuario_id = int(input('Digite o ID do usuário: '))
    novo_username = input('Digite o novo username: ')
    dados_atualizados = {"username": novo_username}
    response = requests.patch(f'https://jsonplaceholder.typicode.com/users/{usuario_id}', json=dados_atualizados)
    print(f"Usuário atualizado: {response.json()}")

def deletar_usuario():
    usuario_id = int(input('Digite o ID do usuário: '))
    response = requests.delete(f'https://jsonplaceholder.typicode.com/users/{usuario_id}')
    print(f"Usuário deletado! Status: {response.status_code}")

def main():
    exibir_menu()
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        listar_usuarios()
    elif opcao == 2:
        listar_tarefas_usuario()
    elif opcao == 3:
        crud_usuario()
    else:
        print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()
