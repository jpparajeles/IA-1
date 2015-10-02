__author__ = 'ia'


from Parser import *


test = Parser();

#el primer parametro indica si es la configuracion inicial o la final, el segundo es el archivo de texto
msg1 = test.parsear('inicial', 'prueba1')
msg2 = test.parsear('final', 'prueba2')


if (msg1 == ''):
    print('Sin errores en config inicial\n')
else:
    print ("Errores en config inicial: \n",msg1)

if (msg2 == ''):
    print('Sin errores en config final\n')
else:
    print ("Errores en config final: \n",msg2)



print("\nPosicion Inicial:\n",test.getPosicionInicial())
print("Posicion final:\n",test.getPosicionFinal())

print('\n\n---------------------------------------')
print('\nPrueba con matrices desde interfaz\n\n')
##para las entradas desde GUI
matriz1 = [[5,5,0,5],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]] #eso viene de GUI
matriz2 = [[4,5,5,5],[1,2,3,4],[1,2,3,0],[1,2,3,4],[1,2,3,4]] #eso viene de GUI
msg1 = test.ParserMatriz('inicial', matriz1)
msg2 = test.ParserMatriz('final', matriz2)
if (msg1 == ''):
    print('Sin errores en config inicial\n')
else:
    print ("Errores en config inicial: \n",msg1)

if (msg2 == ''):
    print('Sin errores en config final\n')
else:
    print ("Errores en config final: \n",msg2)



print("\nPosicion Inicial:\n",test.getPosicionInicial())
print("Posicion final:\n",test.getPosicionFinal())

