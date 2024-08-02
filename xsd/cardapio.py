from xml.dom.minidom import parse
dom=parse("cardapio.xml")

cardapio= dom.documentElement

pratos = cardapio.getElementsByTagName('prato')

id_prato = 0

for prato in pratos:
    id_prato+=1
    categoria= prato.getAttribute ('categoria')
    elemento_nome = prato.getElementsByTagName('Título')[0]
    nome =  elemento_nome.firstChild.nodeValue
    print (f'{id_prato}- {nome}')
    

id_opçao = int(input("Digite a opção que deseja saber mais informações:"))
prato = pratos[id_opçao-1]
print("---\n")
elemento_nome = prato.getElementsByTagName('título')[0]
nome = elemento_nome.firstChild.nodeValue
elemento_ano = prato.getElementsByTagName('ano')[0]
ano = elemento_ano.firstChild.nodeValue
print("Categoria:", categoria)
print("Título:", nome)
