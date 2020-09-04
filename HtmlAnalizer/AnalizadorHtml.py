from HtmlAnalizer.Token import Token
from HtmlAnalizer.Token import Tipo as TT
from Errores.Error import Error
from Errores.Error import Tipo as TE

class Analizador:
    lista_tokens = list()
    lista_errores = list()
    estado = 0 
    lexema = ""
    fila = 0
    columna = 0
    
    def __init__(self):  
        print("INICIO DE ANALISIS HTML")

    def lexer(self,entrada):
        self.entrada = entrada + '$'
        self.caracter = ''
        pos = 0
        
        while pos < len(self.entrada[pos]):
            self.caracter = self.entrada[pos]
            
            # Estado 0
            if self.caracter == "<":
                self.addToken(self.caracter,TT.MENORQUE)
            elif self.caracter == ">":
                self.addToken(self.caracter,TT.MAYORQUE)
            elif self.caracter == "/":
                self.addToken(self.caracter,TT.DIAGONAL)
            elif self.caracter == "=":
                self.addToken(self.caracter,TT.IGUAL)
            elif self.caracter == "\"":
                self.addToken(self.caracter,TT.COMILLAS)
            elif self.caracter == ":":
                self.addToken(self.caracter,TT.DOSPUNTOS)
        
        print(self.entrada)
        return True

    def addError(self, lexema,tipo):
        return 0
    
    def addToken(self, lexema, tipo):
        return 0 