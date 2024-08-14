import json

def carregar_dados(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        return json.load(file)

def exibir_menu(imobiliaria_data):
    print(10 * '-=' + ' MENU ' + '-=' * 10)
    qtd_elementos = len(imobiliaria_data['imobiliaria']['imovel'])

    for i in range(qtd_elementos):
        descricao = imobiliaria_data['imobiliaria']['imovel'][i]['descricao']
        print(f'{descricao} - {i + 1}')
    print('-=' * 20)
    print('')

def exibir_detalhes_imovel(imovel):
    descricao = imovel['descricao']
    nome = imovel['proprietario']['nome']
    email = imovel['proprietario'].get('email', '')
    telefone = imovel['proprietario'].get('telefone', [])
    rua = imovel['endereco']['rua']
    bairro = imovel['endereco']['bairro']
    cidade = imovel['endereco']['cidade']
    numero = imovel['endereco'].get('numero', '')
    tamanho = imovel['caracteristicas']['tamanho']
    numQuartos = imovel['caracteristicas']['numQuartos']
    numBanheiros = imovel['caracteristicas']['numBanheiros']
    valor = imovel['valor']

    print(f"Descrição: {descricao}")
    print(f"Nome: {nome}")
    if email:
        print(f"Email: {email}")
    if telefone:
        if isinstance(telefone, list):
            for t in telefone:
                print(f"Telefone: {t}")
        else:
            print(f"Telefone: {telefone}")
    print(f"Rua: {rua}")
    print(f"Bairro: {bairro}")
    print(f"Cidade: {cidade}")
    print(f"Número: {numero}")
    print(f"Tamanho: {tamanho} m²")
    print(f"Número de Quartos: {numQuartos}")
    print(f"Número de Banheiros: {numBanheiros}")
    print(f"Valor: {valor}")

def programa_interativo(json_file):
    imobiliaria_data = carregar_dados(json_file)
    exibir_menu(imobiliaria_data)

    try:
        imovel_escolhido = int(input('Digite o ID do imóvel para saber mais detalhes: ')) - 1
        print('')
        
        if imovel_escolhido >= 0 and imovel_escolhido < len(imobiliaria_data['imobiliaria']['imovel']):
            imovel = imobiliaria_data['imobiliaria']['imovel'][imovel_escolhido]
            exibir_detalhes_imovel(imovel)
        else:
            print("ID inválido. Por favor, tente novamente.")
    except ValueError:
        print("Por favor, insira um número válido.")

# Caminho do arquivo JSON da imobiliária
json_file = 'parsers/imobiliariaParse.json'

# Executa o programa interativo
programa_interativo(json_file)
