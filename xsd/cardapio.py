from xml.dom.minidom import parse

# Função auxiliar para buscar elementos com namespace
def get_elements_by_tag_name_ns(parent, ns, tag_name):
    return parent.getElementsByTagNameNS(ns, tag_name)

# Carrega o XML
dom = parse("cardapio.xml")

# Define o namespace
namespace = "http://cardapio.org"

# Obtém o elemento raiz
cardapio = dom.documentElement

# Obtém todos os elementos 'prato'
pratos = get_elements_by_tag_name_ns(cardapio, namespace, 'prato')

# Inicializa o id_prato
id_prato = 0

# Itera sobre os pratos
for prato in pratos:
    id_prato += 1
    nome_elem = get_elements_by_tag_name_ns(prato, namespace, 'nome')[0]
    nome = nome_elem.firstChild.nodeValue
    print(f'{id_prato} - {nome}')

# Solicita a opção do usuário
id_opcao = int(input("Digite a opção que deseja saber mais informações: "))
prato = pratos[id_opcao - 1]
print("---\n")

# Obtém as informações do prato selecionado
nome_elem = get_elements_by_tag_name_ns(prato, namespace, 'nome')[0]
nome = nome_elem.firstChild.nodeValue
descricao_elem = get_elements_by_tag_name_ns(prato, namespace, 'descricao')[0]
descricao = descricao_elem.firstChild.nodeValue
ingredientes_elem = get_elements_by_tag_name_ns(prato, namespace, 'ingredientes')[0]
ingredientes = [ing.firstChild.nodeValue for ing in get_elements_by_tag_name_ns(ingredientes_elem, namespace, 'ingrediente')]
preco_elem = get_elements_by_tag_name_ns(prato, namespace, 'preco')[0]
preco = preco_elem.firstChild.nodeValue
calorias_elem = get_elements_by_tag_name_ns(prato, namespace, 'calorias')[0]
calorias = calorias_elem.firstChild.nodeValue
tempo_preparo_elem = get_elements_by_tag_name_ns(prato, namespace, 'tempoPreparo')[0]
tempo_preparo = tempo_preparo_elem.firstChild.nodeValue

# Imprime as informações do prato selecionado
print("Nome:", nome)
print("Descrição:", descricao)
print("Ingredientes:", ", ".join(ingredientes))
print("Preço:", preco)
print("Calorias:", calorias)
print("Tempo de Preparo:", tempo_preparo)
