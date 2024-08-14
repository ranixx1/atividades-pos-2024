from xml.dom.minidom import parse

def get_elements_by_tag_name_ns(parent, ns, tag_name):
    return parent.getElementsByTagNameNS(ns, tag_name)

dom = parse("cardapio.xml")

namespace = "http://cardapio.org"

cardapio = dom.documentElement

pratos = get_elements_by_tag_name_ns(cardapio, namespace, 'prato')
id_prato = 0
for prato in pratos:
    id_prato += 1
    nome_elem = get_elements_by_tag_name_ns(prato, namespace, 'nome')[0]
    nome = nome_elem.firstChild.nodeValue
    print(f'{id_prato} - {nome}')

id_opcao = int(input("Digite a opção que deseja saber mais informações: "))
prato = pratos[id_opcao - 1]
print("---\n")

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

print("Nome:", nome)
print("Descrição:", descricao)
print("Ingredientes:", ", ".join(ingredientes))
print("Preço:", preco)
print("Calorias:", calorias)
print("Tempo de Preparo:", tempo_preparo)
