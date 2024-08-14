import json
import os

# Função para carregar os dados dos usuários do arquivo JSON
def carregar_dados():
    if os.path.exists('usuarios.json'):
        with open('usuarios.json', 'r') as file:
            return json.load(file)
    else:
        return []

# Função para salvar os dados dos usuários no arquivo JSON
def salvar_dados(usuarios):
    with open('usuarios.json', 'w') as file:
        json.dump(usuarios, file, indent=4)

# Função para listar todos os usuários
def listar_usuarios():
    usuarios = carregar_dados()
    if usuarios:
        for usuario in usuarios:
            print(f"ID: {usuario['id']}, Nome: {usuario['name']}, Email: {usuario['email']}")
    else:
        print("Nenhum usuário encontrado.")
    print("")

# Função para listar as tarefas de um usuário específico
def listar_tarefas_usuario():
    usuarios = carregar_dados()
    usuario_id = int(input("Digite o ID do usuário: "))
    usuario = next((u for u in usuarios if u['id'] == usuario_id), None)
    if usuario:
        if 'todos' in usuario:
            print("Tarefas do usuário:")
            for tarefa in usuario['todos']:
                print(f"- {tarefa['title']}")
        else:
            print("O usuário não possui tarefas.")
    else:
        print("Usuário não encontrado.")
    print("")

# Função para criar um novo usuário
def criar_usuario():
    usuarios = carregar_dados()
    novo_id = max([u['id'] for u in usuarios] + [0]) + 1
    nome = input("Digite o nome: ")
    username = input("Digite o username: ")
    email = input("Digite o email: ")
    telefone = input("Digite o telefone: ")

    novo_usuario = {
        "id": novo_id,
        "name": nome,
        "username": username,
        "email": email,
        "phone": telefone,
        "address": {
            "street": "",
            "suite": "",
            "city": "",
            "zipcode": "",
            "geo": {
                "lat": "",
                "lng": ""
            }
        },
        "website": "",
        "company": {
            "name": "",
            "catchPhrase": "",
            "bs": ""
        },
        "todos": []  # Lista de tarefas do usuário
    }

    usuarios.append(novo_usuario)
    salvar_dados(usuarios)
    print("Usuário criado com sucesso!\n")

# Função para ler dados de um usuário específico
def ler_usuario():
    usuarios = carregar_dados()
    usuario_id = int(input("Digite o ID do usuário: "))
    usuario = next((u for u in usuarios if u['id'] == usuario_id), None)
    if usuario:
        print(json.dumps(usuario, indent=4))
    else:
        print("Usuário não encontrado.")
    print("")

# Função para atualizar dados de um usuário específico
def atualizar_usuario():
    usuarios = carregar_dados()
    usuario_id = int(input("Digite o ID do usuário: "))
    usuario = next((u for u in usuarios if u['id'] == usuario_id), None)
    if usuario:
        nome = input(f"Digite o novo nome ({usuario['name']}): ")
        username = input(f"Digite o novo username ({usuario['username']}): ")
        email = input(f"Digite o novo email ({usuario['email']}): ")
        telefone = input(f"Digite o novo telefone ({usuario['phone']}): ")

        if nome: usuario['name'] = nome
        if username: usuario['username'] = username
        if email: usuario['email'] = email
        if telefone: usuario['phone'] = telefone

        salvar_dados(usuarios)
        print("Usuário atualizado com sucesso!\n")
    else:
        print("Usuário não encontrado.")
    print("")

# Função para deletar um usuário específico
def deletar_usuario():
    usuarios = carregar_dados()
    usuario_id = int(input("Digite o ID do usuário: "))
    usuario = next((u for u in usuarios if u['id'] == usuario_id), None)
    if usuario:
        usuarios = [u for u in usuarios if u['id'] != usuario_id]
        salvar_dados(usuarios)
        print("Usuário deletado com sucesso!\n")
    else:
        print("Usuário não encontrado.")
    print("")

# Função para o menu principal da CLI
def menu():
    while True:
        print("Escolha uma opção:")
        print("1. Listar todos usuários")
        print("2. Listar as tarefas de um usuário específico")
        print("3. Criar um novo usuário")
        print("4. Ler dados de um usuário específico")
        print("5. Atualizar um usuário")
        print("6. Deletar um usuário")
        print("7. Sair")
        
        opcao = input("Digite o número da opção: ")
        
        if opcao == '1':
            listar_usuarios()
        elif opcao == '2':
            listar_tarefas_usuario()
        elif opcao == '3':
            criar_usuario()
        elif opcao == '4':
            ler_usuario()
        elif opcao == '5':
            atualizar_usuario()
        elif opcao == '6':
            deletar_usuario()
        elif opcao == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()
