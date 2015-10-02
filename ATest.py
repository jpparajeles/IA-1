__author__ = 'jparajeles'

from AEstrella.AEstrella import busqueda, h, busquedaT
from AEstrella.Nodo import Nodo
from TowerP.Tower import Tower, printBeauty
import timeit

d=Tower(
[['n','n','n','e'],
['a','a','A','a'],
['a','r','v','A'],
['A','v','r','r'],
['r','v','A','v']])
final=Tower(
[['n','n','n','e'],
['a','v','A','r'],
['a','v','A','r'],
['a','v','A','r'],
['a','v','A','r']])


level1=Tower( #0.4-0.5s
[['n','n','n','e'],
['a','A','v','r'],
['a','v','A','r'],
['a','v','A','r'],
['a','v','A','r']])

level2=Tower( #0.9s
[['n','n','n','e'],
['a','v','A','r'],
['a','A','v','r'],
['a','v','A','r'],
['a','v','A','r']])

level3=Tower( #1.7s
[['n','n','n','e'],
['a','v','A','r'],
['a','v','A','r'],
['a','A','v','r'],
['a','v','A','r']])

level4=Tower( #18.8s
[['n','n','n','e'],
['a','v','A','r'],
['a','v','A','r'],
['a','v','A','r'],
['a','A','v','r']])

level=Tower(
[['n','n','n','e'],
['a','A','v','r'],
['a','A','v','r'],
['a','A','v','r'],
['a','A','v','r']])

level12=Tower( #18.8s
[['n','n','n','e'],
['a','A','v','r'],
['a','A','v','r'],
['a','v','A','r'],
['a','v','A','r']])

level13=Tower( #18.8s
[['n','n','n','e'],
['a','A','v','r'],
['a','v','A','r'],
['a','A','v','r'],
['a','v','A','r']])

level14=Tower( #18.8s
[['n','n','n','e'],
['a','A','v','r'],
['a','v','A','r'],
['a','v','A','r'],
['a','A','v','r']])


level23=Tower(
[['n','n','n','e'],
['a','v','A','r'],
['a','A','v','r'],
['a','A','v','r'],
['a','v','A','r']])

level24=Tower(
[['n','n','n','e'],
['a','v','A','r'],
['a','A','v','r'],
['a','v','A','r'],
['a','A','v','r']])

level34=Tower(
[['n','n','n','e'],
['a','v','A','r'],
['a','v','A','r'],
['a','A','v','r'],
['a','A','v','r']])

easy=Tower( #0.5s
[['n','n','n','r'],
['a','a','v','e'],
['r','v','A','A'],
['a','v','A','r'],
['a','v','A','r']])

test = Tower( #0.4s
[['n','n','n','e'],
['a','v','r','A'],
['a','v','A','r'],
['a','v','A','r'],
['a','v','A','r']])

test2 = Tower( #0.7s
[['n','n','n','e'],
['a','v','A','r'],
['a','v','r','A'],
['a','v','A','r'],
['a','v','A','r']])

bio = Tower(
[['n','n','n','e'],
['a','v','r','A'],
['v','A','r','a'],
['a','v','A','r'],
['a','r','A','v']])

test3=Tower(
[['n','n','n','e'],
['a','v','A','r'],
['a','v','A','r'],
['a','v','A','r'],
['v','r','a','A']])


level123=Tower(
[['n','n','n','e'],
['a','A','v','r'],
['a','A','v','r'],
['a','A','v','r'],
['a','v','A','r']])

level124=Tower(
[['n','n','n','e'],
['a','A','v','r'],
['a','A','v','r'],
['a','v','A','r'],
['a','A','v','r']])

#"""

tt = easy

newNodo = Nodo(tt, None, 0, None)
finNodo = Nodo(final, None, 0, None)
newNodo.H=h(newNodo.toDict(), finNodo.toDict())
print(newNodo.H)
print()
start = timeit.default_timer()
result = busquedaT(tt,final)

#result = busqueda(final,tt)
print("Resultado")
print(result.f())
printBeauty(result.Modelo.matrix)
stop = timeit.default_timer()

print (stop - start)
print(result.G)
print(result.f())
#"""

def Analisis(resulta):
    ini = resulta
    print("Desglose")
    conteo = 0
    while ini:
        print("************************")
        printBeauty(ini.Modelo.matrix)
        print("************************")
        try:
            print(ini.Move.description)
            #print("G",ini.g, "H", ini.H)
        except:
            print("inicial")
        print(ini.G)
        print(ini.H)
        ini = ini.Padre
        conteo +=1
    print()
    print("LEN")
    print(conteo)


Analisis(result)
