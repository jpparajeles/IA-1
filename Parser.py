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

    def readFile(self, url):
        if url == "":
            return
        f = open(url)

        textoLeido = f.read()
        f.close()
        return textoLeido




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
    def revisarEstructura(self):
        self.texto = re.sub(r"[\n]+","\n", self.texto)
        self.texto = re.sub(r"[ ]+"," ", self.texto)
        matchObj = re.match( r'var:[a-zA-Z\n\t ]+;[\n\t ]+ini:[a-zA-Z\n\t ]+;[\n\t ]+fin:[a-zA-Z\n\t ]+;[\n\t ]+$', self.texto, re.I)
        if matchObj:
            return ""
        else:
            return "La estructura general tiene error(es). Recuerde colocar las etiquetas y cerrar con ';' cada bloque."





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



    #antes de ejecutar este texto se debe haber asegurado de que el archivo de texto está bien construido
    #si no se hace, fallarán las expresiones regulares
    def setPosiciones(self):
        iniMatch = re.search(r'ini:[a-zA-Z\n\t ]+;', self.texto)
        inicio = self.texto[iniMatch.start()+5:iniMatch.end()-1]
        self.posicionInicial = [ re.split(r' ', x, maxsplit=3) for x in re.split(r'\n', inicio) ]

        finMatch = re.search(r'fin:[a-zA-Z\n\t ]+;', self.texto)
        final = self.texto[finMatch.start()+5:finMatch.end()-1]
        self.posicionFinal = [ re.split(r' ', x, maxsplit=3) for x in re.split(r'\n', final)]

        ##se revisa que las posciiones sean matrices de 5x5
        if (len(self.posicionInicial)==5):
            for elemento in self.posicionInicial:
              if ((len(elemento) != 4) | ('' in elemento)):
                  return "Error en la matriz de posiciones iniciales"
        else:
            return "Error en la matriz de posiciones iniciales"

        #se sustituyen las variables del usuario por sus equivalentes en las variables del sistema
        #se revisa que cada una de las variables haya sido definida por el usuario
        error = ''
        for i in range(0, len(self.posicionInicial)):
            for j in range(0, len(self.posicionInicial[i])):
                if (self.posicionInicial[i][j] not in self.variablesUsuario.keys()):
                    error += "Uso de la variable '" + self.posicionInicial[i][j] + "' no definida por el usuario.\n"
                else:
                    self.posicionInicial[i][j] = self.variablesSistema[  self.variablesUsuario[self.posicionInicial[i][j]]]

        for i in range(0, len(self.posicionFinal)):
            for j in range(0, len(self.posicionFinal[i])):
                if (self.posicionFinal[i][j] not in self.variablesUsuario.keys()):
                    error += "Uso de la variable '" + self.posicionFinal[i][j] + "' no definida por el usuario.\n"
                else:
                    self.posicionFinal[i][j] = self.variablesSistema[  self.variablesUsuario[self.posicionFinal[i][j]]]

    ##se revisa que haya 4 variables de cada color, 1 del espacio, y 3 de barrera (en las posiciones iniciales y finales)
        for variable in self.variablesSistema.values():
            error += str(self.contarVariables(variable, 'inicial'))
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









