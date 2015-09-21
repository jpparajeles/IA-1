__author__ = 'ia'


from Parser import *


##TEST: muestra de como deben ser ejecutado el Parser
#test = Parser("/home/ia/Projects/IA-1/prueba1");
test = Parser("prueba1");
msg = test.parsear();
if (msg == ''):
    print('Sin errores\n')
else:
    print (msg+ "\n")

print("¿El archivo de texto incluye la configuración inicial? " + str(test.getHayConfigInicial()))
print("¿El archivo de texto incluye la configuración final? " + str(test.getHayConfigFinal()))

print("\nPosicion Inicial:\n",test.getPosicionInicial())
print("Posicion final:\n",test.getPosicionFinal())