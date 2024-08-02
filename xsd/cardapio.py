from xml.dom.minidom import parse
dom=parse("cardapio.xml")

cardapio= dom.documentElement

pratos = cardapio.getElementsByTagName('prato')

id_prato = 0

for prato in pratos:
    id_prato+=1
    categoria= prato.getAttribute ('categoria')
    elemento_titulo = prato.getElementsByTagName('Título')[0]
    titulo =  elemento_titulo.firstChild.nodeValue
    print (f'{id_prato}- {titulo}')
    

id_opçao = int(input("Digite a opção que deseja saber mais informações:"))
prato = pratos[id_opçao-1]
print("---\n")
elemento_titulo = prato.getElementsByTagName('título')[0]
titulo = elemento_titulo.firstChild.nodeValue
elemento_ano = prato.getElementsByTagName('ano')[0]
print("Categoria:", categoria)
print("Título:", titulo)
