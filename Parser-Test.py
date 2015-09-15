__author__ = 'ia'


from Parser import *


##TEST: muestra de como deben ser ejecutado el Parser
test = Parser("/home/ia/Projects/IA-1/prueba1");
msg = test.parsear();
if (msg == ''):
    print('Sin errores\n')
else:
    print (msg)
print("Posicion Inicial:\n",test.getPosicionFinal())
print("Posicion final:\n",test.getPosicionInicial())