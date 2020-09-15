from Errores.Error import Error
from Errores.Error import Tipo as TE
from JsAnalizer.Token import Token
from JsAnalizer.Token import Tipo as TT

class Analizador:
    lista_tokens = list()
    lista_errores = list()
    estado = 0 
    lexema = ""
    fila = 0
    columna = 0
    cadenaCorrecta = ""
    bandera = True
    
    def __init__(self):  
        print("INICIO DE ANALISIS RMT")
        
    def lexer(self,entrada):
        while len(self.lista_tokens) > 0 : self.lista_tokens.pop()
        while len(self.lista_errores) > 0 : self.lista_errores.pop()
        self.entrada = entrada + '$'
        self.caracter = ''
        pos = 0
        
        while pos < len(self.entrada):
            self.caracter = self.entrada[pos]
        
            # Estado 0
            if self.estado == 0:
                # Simbolos 
                # Comparacion con igual
                if self.caracter == "*":
                    self.columna += 1
                    self.addToken(self.caracter,TT.ASTERISCO)
                elif self.caracter == "(":
                    self.columna += 1
                    self.addToken(self.caracter,TT.PARENIZQ)
                elif self.caracter == ")":
                    self.columna += 1
                    self.addToken(self.caracter,TT.PARENDER)
                elif self.caracter == "+":
                    self.columna += 1
                    self.addToken(self.caracter,TT.MAS)
                elif self.caracter == "-":
                    self.columna += 1
                    self.addToken(self.caracter,TT.MENOS)
                elif self.caracter == "/":
                    self.columna += 1
                    self.lexema += self.caracter
                    self.addToken(self.caracter,TT.DIAGONAL)
                # Numeros
                elif self.caracter.isnumeric():
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 1
                # Palabras
                elif self.caracter.isalpha():
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 3
                # Delimitadores
                elif self.caracter == " ":
                    self.columna += 1
                    self.cadenaCorrecta += self.caracter
                elif self.caracter == "\t":
                    self.columna += 4
                    self.cadenaCorrecta += self.caracter
                elif self.caracter == "\n":
                    self.columna = 0
                    self.fila += 1
                    self.cadenaCorrecta += self.caracter
                # Errores o final de la cadena
                else:
                    if self.caracter == "$" and pos == len(self.entrada)-1:
                        print("Final")
                    else:
                        self.columna += 1
                        self.addError(self.caracter,TE.CARACTERINVALIDO)
                        self.bandera = False
                
            # Estado 1 a 2 - numeros
            elif self.estado == 1:
                if self.caracter.isnumeric():
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 1
                elif self.caracter == "." and self.entrada[pos+1].isnumeric():
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 2
                else:
                    pos -= 1
                    self.addToken(self.lexema,TT.NUMERO)
                    
            elif self.estado == 2:
                if self.caracter.isnumeric():
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 2
                else:
                    pos -= 1
                    self.addToken(self.lexema,TT.NUMERO)
                    
            # Estado 3 - PR e ID 
            elif self.estado == 3:
                if self.caracter.isalpha() or self.caracter.isnumeric():
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 3
                elif self.caracter == "-":
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 3
                else:
                    pos -= 1
                    self.addToken(self.lexema,TT.ID)
            pos += 1
        print("Finalizo RMT")
            
    def addError(self, lexema,tipo):
        self.bandera = False
        newError = Error(tipo,lexema,self.fila,self.columna)
        self.lista_errores.append(newError)
        self.estado = 0
        self.lexema = ""
    
    def addToken(self, lexema, tipo):
        self.cadenaCorrecta += lexema
        newToken = Token(tipo,lexema,self.fila,self.columna)
        self.lista_tokens.append(newToken)
        self.estado = 0
        self.lexema = ""