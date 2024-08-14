import xml.etree.ElementTree as ET
import json

# Função para converter o XML em um dicionário Python
def xml_to_dict(element):
    if len(element) == 0:
        return element.text

    result = {}
    for child in element:
        child_result = xml_to_dict(child)
        if child.tag in result:
            if not isinstance(result[child.tag], list):
                result[child.tag] = [result[child.tag]]
            result[child.tag].append(child_result)
        else:
            result[child.tag] = child_result
    return result

# Função para fazer o parse do XML e salvar como JSON
def parse_xml_to_json(xml_file, json_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Converte o XML para um dicionário Python
    imobiliaria_dict = {root.tag: xml_to_dict(root)}

    # Salva o dicionário como JSON
    with open(json_file, 'w', encoding='utf-8') as json_f:
        json.dump(imobiliaria_dict, json_f, ensure_ascii=False, indent=4)

# Função para carregar e exibir o menu com os imóveis
def display_menu(json_file):
    with open(json_file, 'r', encoding='utf-8') as imobiliaria_json:
        imobiliaria_data = json.load(imobiliaria_json)

    print(10 * '-=' + ' MENU ' + '-=' * 10)
    qtd_elementos = len(imobiliaria_data['imobiliaria']['imovel'])

    for i in range(qtd_elementos):
        descricao = imobiliaria_data['imobiliaria']['imovel'][i]['descricao']
        print(f'{descricao} - {i + 1}')
    print('-=' * 20)
    print('')

    imovel_escolhido = int(input('Digite o ID do imóvel para saber mais detalhes: ')) - 1
    print('')

    imovel = imobiliaria_data['imobiliaria']['imovel'][imovel_escolhido]

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
    print(f"Tamanho: {tamanho}")
    print(f"Número de Quartos: {numQuartos}")
    print(f"Número de Banheiros: {numBanheiros}")
    print(f"Valor: {valor}")

# Caminho dos arquivos XML e JSON
xml_file = 'parsers/imobiliaria.xml'
json_file = 'parsers/imobiliariaParse.json'

# Parse do XML para JSON
parse_xml_to_json(xml_file, json_file)

# Exibição do menu
display_menu(json_file)
