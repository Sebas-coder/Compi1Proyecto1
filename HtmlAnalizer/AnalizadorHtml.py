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
    bandera = True
    Path = ""
    cadenaCorrecta = ""
    
    def __init__(self):  
        print("INICIO DE ANALISIS HTML")

    def lexer(self,entrada):
        while len(self.lista_tokens) > 0 : self.lista_tokens.pop()
        while len(self.lista_errores) > 0 : self.lista_errores.pop()
        self.entrada = entrada + '$'
        self.caracter = ''
        pos = 0
        cont_Ruta = 1
        
        while pos < len(self.entrada):
            self.caracter = self.entrada[pos]
            
            # Estado 0
            if self.estado == 0:
                if self.caracter == "<":
                    if self.entrada[pos + 1] == "!" and self.entrada[pos + 2] == "-" and self.entrada[pos + 3] == "-":
                        self.lexema += "<!-"
                        pos += 3
                        self.estado = 4
                    else:
                        self.columna += 1
                        self.addToken(self.caracter,TT.MENORQUE)
                elif self.caracter == ">":
                    self.columna += 1
                    self.addToken(self.caracter,TT.MAYORQUE)
                elif self.caracter == "/":
                    self.columna += 1
                    self.addToken(self.caracter,TT.DIAGONAL)
                elif self.caracter == "=":
                    self.columna += 1
                    self.addToken(self.caracter,TT.IGUAL)
                elif self.caracter == ":":
                    self.columna += 1
                    self.addToken(self.caracter,TT.DOSPUNTOS)
                # Cadenas
                elif self.caracter == "\"":
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 1
                # Palabras y valores
                elif self.caracter.isalpha():
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 2
                # Numeros 
                elif self.caracter.isnumeric():
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
                        self.addToken(self.caracter,TT.SIMBOLO)
            # Estado 1 - cadenas
            elif self.estado == 1: 
                if self.caracter == "$" and pos == len(self.entrada)-1:
                    self.addError(self.lexema,TE.ERERRONEA)
                if self.caracter != "\"":
                    self.columna += 1
                    self.lexema += self.caracter
                    if self.caracter == "\n":
                        fila += 1
                        columna = 0  
                else:
                    self.columna += 1
                    self.lexema += self.caracter
                    self.addToken(self.lexema,TT.CADENA)
                    
            # Estado 2 - PR
            elif self.estado == 2:
                if self.caracter.isalpha():
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 2
                else:
                    pos -= 1
                    if self.lexema.lower() == "html":
                        self.addToken(self.lexema,TT.HTML)
                    elif self.lexema.lower() == "head":
                        self.addToken(self.lexema,TT.HEAD)
                    elif self.lexema.lower() == "title":
                        self.addToken(self.lexema,TT.TITLE)
                    elif self.lexema.lower() == "body":
                        self.addToken(self.lexema,TT.BODY)
                    elif self.lexema.lower() == "h":
                        self.addToken(self.lexema,TT.H)
                    elif self.lexema.lower() == "p":
                        self.addToken(self.lexema,TT.P)
                    elif self.lexema.lower() == "br":
                        self.addToken(self.lexema,TT.BR)
                    elif self.lexema.lower() == "img":
                        self.addToken(self.lexema,TT.IMG)
                    elif self.lexema.lower() == "src":
                        self.addToken(self.lexema,TT.SRC)
                    elif self.lexema.lower() == "a":
                        self.addToken(self.lexema,TT.A)
                    elif self.lexema.lower() == "ol":
                        self.addToken(self.lexema,TT.O)
                    elif self.lexema.lower() == "ul":
                        self.addToken(self.lexema,TT.UL)
                    elif self.lexema.lower() == "li":
                        self.addToken(self.lexema,TT.LI)
                    elif self.lexema.lower() == "style":
                        self.addToken(self.lexema,TT.STYLE)
                    elif self.lexema.lower() == "table":
                        self.addToken(self.lexema,TT.TABLE)
                    elif self.lexema.lower() == "th":
                        self.addToken(self.lexema,TT.TH)
                    elif self.lexema.lower() == "tr":
                        self.addToken(self.lexema,TT.TR)
                    elif self.lexema.lower() == "td":
                        self.addToken(self.lexema,TT.TD)
                    elif self.lexema.lower() == "caption":
                        self.addToken(self.lexema,TT.CAPTION)
                    elif self.lexema.lower() == "col":
                        self.addToken(self.lexema,TT.COL)
                    elif self.lexema.lower() == "thead":
                        self.addToken(self.lexema,TT.THEAD)
                    elif self.lexema.lower() == "tbody":
                        self.addToken(self.lexema,TT.TBODY)
                    elif self.lexema.lower() == "tfoot":
                        self.addToken(self.lexema,TT.TFOOT)
                    else:
                        self.addToken(self.lexema,TT.VALOR)
                        
            # Estado 3 - Numeros 
            elif self.estado == 3:
                if self.caracter.isnumeric():
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 3
                else: 
                    pos -= 1
                    self.addToken(self.lexema,TT.VALOR)
            # Estado 4 - Comentarios 
            elif self.estado == 4:
                if self.caracter == "$" and pos == len(self.entrada)-1:
                        self.addError(self.lexema,TE.ERERRONEA)
                elif self.caracter != "-":
                    if self.caracter == "\n":
                        self.columna = 0
                        self.fila += 1
                    else:
                        self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 4
                elif self.entrada[pos + 1] == "-" and self.entrada[pos + 2] == ">":
                    if cont_Ruta == 1:
                        cont_Ruta += 1
                    elif cont_Ruta == 2:
                        self.Path = self.lexema.lstrip("<!--PATHL:")
                        self.Path = self.Path.rstrip("-->" )
                        self.Path = self.Path.strip()
                        cont_Ruta = 0
                    self.columna += 3
                    pos += 2
                    self.lexema += "-->"
                    self.addToken(self.lexema,TT.COMENTARIO)
                else: 
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 4
            pos += 1
        print("COCHEE")

    def addError(self, lexema,tipo):
        newError = Error(tipo,lexema)
        self.lista_errores.append(newError)
        self.estado = 0
        self.lexema = ""
    
    def addToken(self, lexema, tipo):
        self.cadenaCorrecta += lexema
        newToken = Token(tipo,lexema)
        self.lista_tokens.append(newToken)
        self.estado = 0
        self.lexema = ""