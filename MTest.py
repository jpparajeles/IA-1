from AEstrella.AEstrella import busqueda

__author__ = 'ia'
from TowerP.Tower import Tower, printBeauty
from Writer import *
# debe leerse de algun lado
final=Tower(
[['n','n','n','e'],
['a','v','A','r'],
['a','v','A','r'],
['a','v','A','r'],
['a','v','A','r']])

# igual que aqui
easy=Tower( #0.5s
[['n','n','n','e'],
['a','a','v','r'],
['r','v','A','A'],
['a','v','A','r'],
['a','v','A','r']])

#se debe llamar a esa funcion
result = busqueda(easy,final)

for elem in result:
    try:
        printBeauty(elem.Move.tower.matrix) #deberia ser la funcion para escribir en archivos
    except:
        printBeauty(easy.matrix) # inicial #deberia ser la funcion para escribir en archivos
    print() #\n


writer = Writer()
writer.writeSolution( easy,result)