from Errores.Error import Error
from Errores.Error import Tipo as TE
from JsAnalizer.Token import Token
from JsAnalizer.Token import Tipo as TT
from Estados.Graficador import Graficador 

class Analizador:
    lista_tokens = list()
    lista_errores = list()
    lista_estados = list()
    lista_grafica = list()
    estado = 0 
    lexema = ""
    fila = 0
    columna = 0
    cadenaCorrecta = ""
    bandera = True
    E1 = True
    E2 = True
    E3 = True
    E4 = True
    E5 = True
    E6 = True
    Cont_ER = 0
    
    def __init__(self):  
        print("INICIO DE ANALISIS JS")

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
                if self.caracter == "=":
                    if self.entrada[pos+1] == "=":
                        self.columna += 2
                        pos += 1
                        self.lexema = "=="
                        self.addToken(self.lexema,TT.IGUALDAD)
                    else:
                        self.columna += 1
                        self.addToken(self.lexema,TT.IGUAL)
                elif self.caracter == "*":
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
                elif self.caracter == "{":
                    self.columna += 1
                    self.addToken(self.caracter,TT.LLAVEIZQ)
                elif self.caracter == "}":
                    self.columna += 1
                    self.addToken(self.caracter,TT.LLAVEDER)
                elif self.caracter == ":":
                    self.columna += 1
                    self.addToken(self.caracter,TT.DOSPUNTOS)
                elif self.caracter == ";":
                    self.columna += 1
                    self.addToken(self.caracter,TT.PUNTOYCOMA)
                elif self.caracter == ".":
                    self.columna += 1
                    self.addToken(self.caracter,TT.PUNTO)
                elif self.caracter == ",":
                    self.columna += 1
                    self.addToken(self.caracter,TT.COMA)
                # Caracteres 
                elif self.caracter == "'":
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 7
                # Cadenas 
                elif self.caracter == "\"":
                    if self.E1:
                        if self.Cont_ER < 3:
                            self.Cont_ER += 1
                            self.lista_grafica.append(1)
                            self.E1 = False
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 8
                # Comparadores 
                elif self.caracter == "<":
                    if self.entrada[pos+1] == "=":
                        self.columna += 2
                        pos += 1
                        self.lexema = "<="
                        self.addToken(self.lexema,TT.MENORIGUAL)
                    else:
                        self.columna += 1
                        self.addToken(self.lexema,TT.MENORQUE)
                elif self.caracter == ">":
                    if self.entrada[pos+1] == "=":
                        self.columna += 2
                        self.lexema = ">="
                        self.addToken(self.lexema,TT.MAYORIGUAL)
                    else:
                        self.columna += 1
                        self.addToken(self.lexema,TT.MENORQUE)
                elif self.caracter == "&":
                    if self.entrada[pos+1] == "&":
                        self.columna += 2
                        pos += 1
                        self.lexema = "&&"
                        self.addToken(self.lexema,TT.CONJUNCION)
                    else:
                        self.columna += 1
                        self.addError(self.caracter,TE.CARACTERINVALIDO)
                elif self.caracter == "|":
                    if self.entrada[pos+1] == "|":
                        self.columna += 2
                        pos += 1
                        self.lexema = "||"
                        self.addToken(self.lexema,TT.DISYUNCION)
                    else:
                        self.columna += 1
                        self.addError(self.caracter,TE.CARACTERINVALIDO)
                # Comentarios
                elif self.caracter == "/":
                    if self.entrada[pos+1] == "/" or  self.entrada[pos+1] == "*":
                        self.columna += 1
                        self.lexema += self.caracter
                        self.estado = 4
                    else:
                        self.columna += 1
                        self.lexema += self.caracter
                        self.addToken(self.caracter,TT.DIAGONAL)
                # Desigualdad                    
                elif self.caracter == "!":
                    if self.entrada[pos+1] == "=":
                        pos += 1
                        self.columna += 1
                        self.lexema += "!="
                        self.addToken(self.lexema,TT.ADMIRACIONIZQ)
                    else: 
                        self.columna += 1
                        self.addToken(self.caracter,TT.ADMIRACIONIZQ)
                # Numeros
                elif self.caracter.isnumeric():
                    if self.E1:
                        if self.Cont_ER < 3:
                            self.Cont_ER += 1
                            self.lista_grafica.append(1)
                            self.E1 = False
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 1
                # Palabras
                elif self.caracter.isalpha():
                    if self.E2:
                        if self.Cont_ER < 3:
                            self.Cont_ER += 1
                            self.lista_grafica.append(1)
                            self.E2 = False
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
                        print("final")
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
                if self.caracter.isalpha():
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 3
                elif self.caracter == "-":
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 3
                else:
                    pos -= 1
                    if self.lexema.lower() == "int":
                        self.addToken(self.lexema,TT.INT)
                    elif self.lexema.lower() == "string":
                        self.addToken(self.lexema,TT.STRING)
                    elif self.lexema.lower() == "char":
                        self.addToken(self.lexema,TT.CHAR)
                    elif self.lexema.lower() == "boolean":
                        self.addToken(self.lexema,TT.BOOLEAN)
                    elif self.lexema.lower() == "type":
                        self.addToken(self.lexema,TT.TYPE)
                    elif self.lexema.lower() == "if":
                        self.addToken(self.lexema,TT.IF)
                    elif self.lexema.lower() == "else":
                        self.addToken(self.lexema,TT.ELSE)
                    elif self.lexema.lower() == "for":
                        self.addToken(self.lexema,TT.FOR)
                    elif self.lexema.lower() == "while":
                        self.addToken(self.lexema,TT.WHILE)
                    elif self.lexema.lower() == "do":
                        self.addToken(self.lexema,TT.DO)
                    elif self.lexema.lower() == "continue":
                        self.addToken(self.lexema,TT.CONTINUE)
                    elif self.lexema.lower() == "break":
                        self.addToken(self.lexema,TT.BREAK)
                    elif self.lexema.lower() == "return":
                        self.addToken(self.lexema,TT.RETURN)
                    elif self.lexema.lower() == "true":
                        self.addToken(self.lexema,TT.TRUE)
                    elif self.lexema.lower() == "false":
                        self.addToken(self.lexema,TT.FALSE)
                    elif self.lexema.lower() == "function":
                        self.addToken(self.lexema,TT.FUNCTION)
                    elif self.lexema.lower() == "constructor":
                        self.addToken(self.lexema,TT.CONSTRUCTOR)
                    elif self.lexema.lower() == "class":
                        self.addToken(self.lexema,TT.CLASS)
                    elif self.lexema.lower() == "math":
                        self.addToken(self.lexema,TT.MATH)
                    elif self.lexema.lower() == "pow":
                        self.addToken(self.lexema,TT.POW)
                    elif self.lexema.lower() == "path":
                        self.addToken(self.lexema,TT.PATH)
                    elif self.lexema.lower() == "this":
                        self.addToken(self.lexema,TT.THIS)
                    else:
                        self.addToken(self.lexema,TT.ID)
            
            # Estado 4 - Comentarios
            elif self.estado == 4:
                if self.caracter == "/":
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 5
                elif self.caracter == "*":
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 6
            
            elif self.estado == 5:
                if self.E3:
                        if self.Cont_ER < 3:
                            self.Cont_ER += 1
                            self.lista_grafica.append(1)
                            self.E3 = False
                            
                if self.caracter != "\n":
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 5
                    if self.caracter == "$" and pos == len(self.entrada)-1:
                        self.addError(self.lexema,TE.ERERRONEA)
                else:
                    self.columna = 0
                    self.fila += 1
                    self.addToken(self.lexema,TT.COMENTUNI)
                    self.estado = 0
                
            elif self.estado == 6:
                if self.E4:
                        if self.Cont_ER < 3:
                            self.Cont_ER += 1
                            self.lista_grafica.append(1)
                            self.E4 = False
                            
                if self.caracter == "$" and pos == len(self.entrada)-1:
                        self.addError(self.lexema,TE.ERERRONEA)
                elif self.caracter != "*":
                    self.columna += 1
                    self.lexema += self.caracter
                    if self.caracter == "\n":
                        self.fila += 1
                        self.columna = 0
                    self.estado = 6
                elif self.entrada[pos +1] == "/":
                    pos += 1
                    self.columna += 2
                    self.lexema += "*/"
                    self.addToken(self.lexema,TT.COMENTMUL)
                    self.estado = 0
                else:
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 6
                    
            # Estado 7 - caracteres
            elif self.estado == 7:
                if self.caracter != " " and self.caracter != "\n" and self.caracter != "\t" and self.entrada[pos +1] != "'":
                    self.columna += 2
                    self.lexema += self.caracter + "'"
                    self.addToken(self.lexema,TT.CARACTER)
                    pos += 1
                    self.estado = 0
                else:
                    pos -= 1
                    self.columna += 1
                    self.addError(self.lexema,TE.CARACTERINVALIDO)
                    self.estado = 0
            # Estado 8 - cadenas
            elif self.estado == 8:
                if self.caracter == "$" and pos == len(self.entrada)-1:
                        self.addError(self.lexema,TE.ERERRONEA)
                elif self.caracter != "\"":
                    self.columna += 1
                    self.lexema += self.caracter
                    if self.caracter == "\n":
                        self.fila += 1
                        self.columna = 0
                    self.estado = 8
                else:
                    self.columna += 1
                    self.lexema += self.caracter
                    self.addToken(self.lexema,TT.CADENA)
            pos += 1
            
        
        gr = Graficador()
        gr.Graficar(self.lista_grafica) 
    
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