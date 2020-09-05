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
    
    def __init__(self):  
        print("INICIO DE ANALISIS CSS")

    def lexer(self,entrada):
        self.entrada = entrada + '$'
        self.caracter = ''
        pos = 0
        
        while pos < len(self.entrada[pos]):
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
                        self.addToken(self.lexema,TT.IGUALDAD)
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
                elif self.caracter == ".":
                    self.columna += 1
                    self.addToken(self.caracter,TT.PUNTO)
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
                        pos += 1
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
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 4
                # Desigualdad                    
                elif self.caracter == "!":
                    self.columna += 1
                    self.addToken(self.caracter,TT.ADMIRACIONIZQ)
                # Numeros
                elif self.caracter.isnumeric():
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 1
                # Palabras
                elif self.isalpha():
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 3
                # Delimitadores
                elif self.caracter == " ":
                    self.columna += 1
                elif self.caracter == "\t":
                    self.columna += 4
                elif self.caracter == "\n":
                    self.columna = 0
                    fila += 1
                # Errores o final de la cadena
                else:
                    if self.caracter == "$" and pos == len(self.entrada)-1:
                        print("final")
                    else:
                        self.addError(self.caracter,TE.CARACTERINVALIDO)
                
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
                else:
                    pos -= 1
                    self.addError(self.caracter,TE.CARACTERINVALIDO)
            
            elif self.estado == 5:
                if self.caracter == "\n":
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 5
                else:
                    self.columna = 0
                    self.fila += 1
                    self.addToken(self.lexema,TT.COMENTUNI)
                    self.estado = 0
                    
            elif self.estado == 6:
                if self.caracter != "*" and self.entrada[pos +1] != "/":
                    self.columna += 1
                    self.lexema += self.caracter
                    if self.caracter == "\n":
                        self.fila += 1
                        self.columna = 0
                    self.estado = 6
                else:
                    self.columna += 2
                    pos += 1
                    self.lexema += "*/"
                    self.addToken(self.lexema,TT.COMENTMUL)
                    self.estado = 0