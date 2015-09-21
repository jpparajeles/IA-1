__author__ = 'ia'
import re
import copy

import sys

class Parser:
    def __init__(self, url):
        self.archivo = url
        self.tabla = []
        self.texto = self.readFile(url)
        self.posicionInicial = []
        self.posicionFinal = []
        self.variablesSistema = {'verde':'v', 'rojo':'r', 'amarillo':'a', 'azul':'A', 'espacio':'e', 'barrera':'n'}
        self.variablesByKey =  {'v': 'verde', 'r': 'rojo', 'a':'amarillo','A':  'azul', 'e': 'espacio', 'n': 'barrera'}
        self.variablesUsuario = {'':'', '':'', '':'', '':'', '':'', '':'', '':''}
        self.hayConfigInicial = False
        self.hayConfigFinal = False


    def readFile(self, url):
        if url == "":
            return
        f = open(url)

        textoLeido = f.read()
        f.close()
        return textoLeido


    def getHayConfigInicial(self):
        return self.hayConfigInicial

    def getHayConfigFinal(self):
        return self.hayConfigFinal


    """ revisarEstructura
        revisara que venga:
    var:
    w color1
    x color2
    y color3
    z color4
    e espacio
    n barrera

    inicial:
    n e e e (etc)

    final:
    n e e e (etc)

    con una expresion regular
    """
    def revisarEstructura(self): #revisa si se ingreso las dos configuraciones (inicial y final) o solo una de ellas (e indica cuál)
        self.texto = re.sub(r"[\n]+","\n", self.texto)
        self.texto = re.sub(r"[ ]+"," ", self.texto)
        matchObj = re.match( r'var:[a-zA-Z\n\t ]+;[\n\t ]+ini:[a-zA-Z\n\t ]+;[\n\t ]+fin:[a-zA-Z\n\t ]+;[\n\t ]+$', self.texto, re.I)
        if matchObj:
            self.hayConfigInicial = True
            self.hayConfigFinal = True
            return ""
        matchObj = re.match( r'var:[a-zA-Z\n\t ]+;[\n\t ]+ini:[a-zA-Z\n\t ]+;[\n\t ]+$', self.texto, re.I)
        if matchObj:
            self.hayConfigInicial = True
            return ""
        matchObj = re.match( r'var:[a-zA-Z\n\t ]+;[\n\t ]+fin:[a-zA-Z\n\t ]+;[\n\t ]+$', self.texto, re.I)
        if matchObj:
            self.hayConfigFinal = True
            return ""
        else:
            return "La estructura general tiene error(es). Recuerde colocar las etiquetas y cerrar con ';' cada bloque. \nSin alguno de estos elementos, no se puede identificar cada una de las partes del archivo"





    def montarVariables(self):
        mensajeError = ""
        varsMatch = re.search(r'var:[a-zA-Z\n\t ]+;', self.texto)
        vars = self.texto[varsMatch.start()+5:varsMatch.end()-1]
        listaVar = [ re.split(r' ', x, maxsplit=2) for x in re.split(r'\n', vars) ]

        listaVarCopia = copy.deepcopy(listaVar)

        for x in range(0, len( listaVarCopia)):
            temp = listaVarCopia[x][0]
            if (temp in [elemento[0] for elemento in listaVarCopia[x+1:]]):
                mensajeError += "No se puede dar dos declaraciones a la  variable: '"+ temp + "' \n"

        self.variablesUsuario = {key: value for (key, value) in listaVar}

        for element in self.variablesUsuario:
            if (self.variablesUsuario[element] not in  self.variablesSistema.keys()):
                mensajeError += "Uso de palabra no existente en el lenguaje: " + self.variablesUsuario[element] + "\n"

        if (len(self.variablesUsuario) < 6):
            mensajeError += "Error en la definición de variables. Falta declarar variables"
        elif (len(self.variablesUsuario) > 6):
            mensajeError += "Error en la definición de variables. Se declaró más variable(s) de las necesarias."

        return mensajeError

    ##se revisa que las posiciones sean matrices de 5x5
    def revisarMatricesPosiciones(self, matriz):
        matrizRev = []
        error = ''
        if matriz == 'inicial':
            matrizRev = self.posicionInicial
        if matriz == 'final':
            matrizRev = self.posicionFinal

        if (len(matrizRev)==5):
            for elemento in matrizRev:
                if ((len(elemento) != 4) | ('' in elemento)):
                    error = "Error en la matriz de posición " + matriz + ". Revise la cantidad de filas y de elementos en cada una de ellas.\n"
                    break
        else:
            error = "Error en la matriz de posición " + matriz + ". Revise la cantidad de filas y de elementos en cada una de ellas.\n"
        return error

    def sustituirVariables(self, posicion):
        matrizRev = []
        error = ''
        if posicion == 'inicial':
            matrizRev = self.posicionInicial ##como Python pasa la referencia, al final no es necesario asignar el valor de matrizRev a self.posicionInicial
        if posicion == 'final':
            matrizRev = self.posicionFinal


        for i in range(0, len(matrizRev)):
            for j in range(0, len(matrizRev[i])):
                if (matrizRev[i][j] not in self.variablesUsuario.keys()):
                    error += "Uso de la variable '" + matrizRev[i][j] + "' no definida por el usuario.\n"
                else:
                    matrizRev[i][j] = self.variablesSistema[  self.variablesUsuario[matrizRev[i][j]]]

        return error

    #antes de ejecutar este texto se debe haber asegurado de que el archivo de texto está bien construido
    #si no se hace, fallarán las expresiones regulares
    def setPosiciones(self):
        if self.hayConfigInicial:
            iniMatch = re.search(r'ini:[a-zA-Z\n\t ]+;', self.texto)
            inicio = self.texto[iniMatch.start()+5:iniMatch.end()-1]
            self.posicionInicial = [ re.split(r' ', x, maxsplit=3) for x in re.split(r'\n', inicio) ]

        if self.hayConfigFinal:
            finMatch = re.search(r'fin:[a-zA-Z\n\t ]+;', self.texto)
            final = self.texto[finMatch.start()+5:finMatch.end()-1]
            self.posicionFinal = [ re.split(r' ', x, maxsplit=3) for x in re.split(r'\n', final)]

        ##se revisa que las posiciones sean matrices de 5x5
        if self.hayConfigInicial:
            msg = self.revisarMatricesPosiciones('inicial')
            if msg != '':
                return msg
        if self.hayConfigFinal:
            msg = self.revisarMatricesPosiciones('final')
            if msg != '':
                return msg
        #se sustituyen las variables del usuario por sus equivalentes en las variables del sistema
        #se revisa que cada una de las variables haya sido definida por el usuario
        error = ''
        if self.hayConfigInicial:
            error += self.sustituirVariables('inicial')
        if self.hayConfigFinal:
            error += self.sustituirVariables('final')


    ##se revisa que haya 4 variables de cada color, 1 del espacio, y 3 de barrera (en las posiciones iniciales y finales)
        if self.hayConfigInicial:
            for variable in self.variablesSistema.values():
                error += str(self.contarVariables(variable, 'inicial'))
        if self.hayConfigFinal:
            for variable in self.variablesSistema.values():
                error += str(self.contarVariables(variable, 'final'))

        return error

    #cuenta cuántas veces aparece una variable en la posicion que se le indica (inicial o final)
    def contarVariables(self, var, posicion):
        contador = 0
        if posicion == 'inicial':
            for fila in self.posicionInicial:
                for celda in fila:
                    if celda == var:
                        contador +=1
        elif posicion == 'final':
            for fila in self.posicionFinal:
                for celda in fila:
                    if celda == var:
                        contador +=1

        if var == "e":
            if contador != 1:
                return ("En posición "+ posicion +": cantidad incorrecta del elemento: 'espacio'\n")
        if var == "n":
            if contador != 3:
                return ("En posición "+ posicion +": cantidad incorrecta del elemento: 'barrera'\n")
        elif (var != "e") & (var != "n"):
            if contador != 4:
                return  ("En posición "+ posicion +": cantidad incorrecta del elemento: '" + self.variablesByKey[var] + "'\n")
        return ""

    def getPosicionInicial(self):
        return self.posicionInicial

    def getPosicionFinal(self):
        return self.posicionFinal


    def parsear(self):
        if (self.archivo == ''):
            return "Para parsear debe elegir un archivo de texto."
        error = self.revisarEstructura()
        if (error==''):
            error = self.montarVariables()
            if (error == ''):
                error = self.setPosiciones()
                return error
            else:
                return error
        else:
            return error









