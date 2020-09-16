from Errores.Error import Error
from Errores.Error import Tipo as TE
from CssAnalizer.Token import Token
from CssAnalizer.Token import Tipo as TT

class Analizador:
    # listas
    lista_tokens = list()
    lista_errores = list()
    lista_estados = list()
    # partes de analisis
    estado = 0 
    Pathlexema = ""
    fila = 0
    columna = 0
    cadenaCorrecta = ""
    bandera = True
    listadoEstados = ""
    Path = ""
    
    def __init__(self):  
        print("INICIO DE ANALISIS CSS")

    def lexer(self,entrada):
        print("AQUI EMPIEZA")
        while len(self.lista_tokens) > 0 : self.lista_tokens.pop()
        while len(self.lista_errores) > 0 : self.lista_errores.pop()
        while len(self.lista_estados) > 0 : self.lista_estados.pop()
        self.entrada = entrada + '$'
        self.caracter = ''
        pos = 0
        cont_Ruta = 1
        
        while pos < len(self.entrada) :
            self.caracter = self.entrada[pos]
            
            # Estado 0
            if self.estado == 0:
                # Simbolos 
                if self.caracter == "{":
                    self.listadoEstados += "S0 - " + self.caracter + " -> S9"
                    self.addEstados(self.listadoEstados)
                    self.columna += 1
                    self.addToken(self.caracter,TT.LLAVEIZQ)
                elif self.caracter == "}":
                    self.listadoEstados += "S0 - " + self.caracter + " -> S9"
                    self.addEstados(self.listadoEstados)
                    self.columna += 1
                    self.addToken(self.caracter,TT.LLAVEDER)
                elif self.caracter == ":":
                    self.listadoEstados += "S0 - " + self.caracter + " -> S9"
                    self.addEstados(self.listadoEstados)
                    self.columna += 1
                    self.addToken(self.caracter,TT.DOSPUNTOS)
                elif self.caracter == ";":
                    self.listadoEstados += "S0 - " + self.caracter + " -> S9"
                    self.addEstados(self.listadoEstados)
                    self.columna += 1
                    self.addToken(self.caracter,TT.PUNTOYCOMA)
                elif self.caracter == ",":
                    self.listadoEstados += "S0 - " + self.caracter + " -> S9"
                    self.addEstados(self.listadoEstados)
                    self.columna += 1
                    self.addToken(self.caracter,TT.COMA)
                elif self.caracter == "(":
                    self.listadoEstados += "S0 - " + self.caracter + " -> S9"
                    self.addEstados(self.listadoEstados)
                    self.columna += 1
                    self.addToken(self.caracter,TT.PARENIZQ)
                elif self.caracter == ")":
                    self.listadoEstados += "S0 - " + self.caracter + " -> S9"
                    self.addEstados(self.listadoEstados)
                    self.columna += 1
                    self.addToken(self.caracter,TT.PARENIZQ)
                elif self.caracter == "*":
                    self.listadoEstados += "S0 - " + self.caracter + " -> S9"
                    self.addEstados(self.listadoEstados)
                    self.columna += 1
                    self.addToken(self.caracter,TT.ASTERISCO)
                elif self.caracter == ".":
                    self.listadoEstados += "S0 - " + self.caracter + " -> S9"
                    self.addEstados(self.listadoEstados)
                    self.columna += 1
                    self.addToken(self.caracter,TT.PUNTO)
                elif self.caracter == "-":
                    self.listadoEstados += "S0 - " + self.caracter + " -> S9"
                    self.addEstados(self.listadoEstados)
                    self.columna += 1
                    self.addToken(self.caracter,TT.MENOS)
                elif self.caracter == "%":
                    self.listadoEstados += "S0 - " + self.caracter + " -> S9"
                    self.addEstados(self.listadoEstados)
                    self.columna += 1
                    self.addToken(self.caracter,TT.PORCENTAJE)
                # Identificadores o colores hexagecimales * 5
                elif self.caracter == "#":
                    if self.entrada[pos + 1].isnumeric() or self.entrada[pos + 1].isalpha():
                        self.lexema += "#"
                        self.columna += 1
                        self.estado = 5
                        self.listadoEstados += "S5 - " + self.caracter 
                    else:
                        self.columna += 1
                        self.addToken(self.caracter,TT.HASH)
                        self.listadoEstados += "S0 - " + self.caracter + " -> S9"
                        self.addEstados(self.listadoEstados)
                # Cadena de texto * 4   
                elif self.caracter == "\"":  
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 4
                    self.listadoEstados += "S0 - " + self.caracter 
                # Comentario * 6
                elif self.caracter == "/":
                    if self.entrada[pos + 1] == "*":
                        self.columna += 1
                        self.lexema += self.caracter
                        self.estado = 6
                        self.listadoEstados += "S0 - " + self.caracter 
                    else:
                        self.columna += 1
                        self.addError(self.caracter,TE.CARACTERINVALIDO)    
                # Numeros * 1 -2
                elif self.caracter.isnumeric():
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 1
                    self.listadoEstados += "S0 - " + self.caracter 
                # Palabras * 3
                elif self.caracter.isalpha():
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 3
                    self.listadoEstados += "S0 - " + self.caracter 
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
                        self.addError(self.caracter,TE.CARACTERINVALIDO)
                        self.bandera = False
                
            # Estado 1 a 2 - numeros
            elif self.estado == 1:
                self.listadoEstados += " -> S1 " 
                if self.caracter.isnumeric():
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 1
                    self.listadoEstados += "- " + self.caracter 
                elif self.caracter == "." and self.entrada[pos+1].isnumeric():
                    self.listadoEstados += "- " + self.caracter 
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 2
                else:
                    self.addEstados(self.listadoEstados)
                    pos -= 1
                    self.addToken(self.lexema,TT.NUMERO)
                    
            elif self.estado == 2:
                self.listadoEstados += " -> S2 " 
                if self.caracter.isnumeric():
                    self.listadoEstados += "- " + self.caracter 
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 2
                else:
                    pos -= 1
                    self.addEstados(self.listadoEstados)
                    self.addToken(self.lexema,TT.NUMERO)
                    
            # Estado 3 - PR e ID 
            elif self.estado == 3:
                self.listadoEstados += " -> S3 " 
                if self.caracter.isalpha():
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 3
                    self.listadoEstados += "- " + self.caracter 
                elif self.caracter == "-":
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 3
                    self.listadoEstados += "- " + self.caracter
                else:
                    self.addEstados(self.listadoEstados)
                    pos -= 1
                    if self.lexema.lower() == "color":
                        self.addToken(self.lexema,TT.COLOR)
                    elif self.lexema.lower() == "background-color":
                        self.addToken(self.lexema,TT.BACKGRCOLOR)
                    elif self.lexema.lower() == "background-image":
                        self.addToken(self.lexema,TT.BACKGRIMAGE)
                    elif self.lexema.lower() == "border":
                        self.addToken(self.lexema,TT.BORDER)
                    elif self.lexema.lower() == "opacity":
                        self.addToken(self.lexema,TT.OPACITY)
                    elif self.lexema.lower() == "background":
                        self.addToken(self.lexema,TT.BACKGROUND)
                    elif self.lexema.lower() == "text-align":
                        self.addToken(self.lexema,TT.TEXTALING)
                    elif self.lexema.lower() == "font-family":
                        self.addToken(self.lexema,TT.FONTFAMILY)
                    elif self.lexema.lower() == "font-style":
                        self.addToken(self.lexema,TT.FONTSTYLE)
                    elif self.lexema.lower() == "font-weight":
                        self.addToken(self.lexema,TT.FONTWEIGHT)
                    elif self.lexema.lower() == "font-size":
                        self.addToken(self.lexema,TT.FONTSIZE)
                    elif self.lexema.lower() == "font":
                        self.addToken(self.lexema,TT.FONT)
                    elif self.lexema.lower() == "padding-left":
                        self.addToken(self.lexema,TT.PADDLEFT)
                    elif self.lexema.lower() == "padding-right":
                        self.addToken(self.lexema,TT.PADDRIGHT)
                    elif self.lexema.lower() == "padding-bottom":
                        self.addToken(self.lexema,TT.PADDBOTTOM)
                    elif self.lexema.lower() == "padding-top":
                        self.addToken(self.lexema,TT.PADDTOP)
                    elif self.lexema.lower() == "padding":
                        self.addToken(self.lexema,TT.PADDING)
                    elif self.lexema.lower() == "display":
                        self.addToken(self.lexema,TT.DISPLAY)
                    elif self.lexema.lower() == "line-height":
                        self.addToken(self.lexema,TT.LINEHEIGHT)
                    elif self.lexema.lower() == "width":
                        self.addToken(self.lexema,TT.WIDTH)
                    elif self.lexema.lower() == "height":
                        self.addToken(self.lexema,TT.HEIGHT)
                    elif self.lexema.lower() == "margin-top":
                        self.addToken(self.lexema,TT.MARGTOP)
                    elif self.lexema.lower() == "margin-right":
                        self.addToken(self.lexema,TT.MARGRIGHT)
                    elif self.lexema.lower() == "margin-bottom":
                        self.addToken(self.lexema,TT.MARGBOTTOM)
                    elif self.lexema.lower() == "margin-left":
                        self.addToken(self.lexema,TT.MARGLEFT)
                    elif self.lexema.lower() == "border-style":
                        self.addToken(self.lexema,TT.BORDERSTYLE)
                    elif self.lexema.lower() == "display":
                        self.addToken(self.lexema,TT.DISPLAY)
                    elif self.lexema.lower() == "position":
                        self.addToken(self.lexema,TT.POSITION)
                    elif self.lexema.lower() == "bottom":
                        self.addToken(self.lexema,TT.BOTTOM)
                    elif self.lexema.lower() == "top":
                        self.addToken(self.lexema,TT.top)
                    elif self.lexema.lower() == "right":
                        self.addToken(self.lexema,TT.RIGHT)
                    elif self.lexema.lower() == "left":
                        self.addToken(self.lexema,TT.LEFT)
                    elif self.lexema.lower() == "float":
                        self.addToken(self.lexema,TT.FLOAT)
                    elif self.lexema.lower() == "clear":
                        self.addToken(self.lexema,TT.CLEAR)
                    elif self.lexema.lower() == "max-width":
                        self.addToken(self.lexema,TT.MAXWIGTH)
                    elif self.lexema.lower() == "min-width":
                        self.addToken(self.lexema,TT.MINWIGTH)
                    elif self.lexema.lower() == "max-height":
                        self.addToken(self.lexema,TT.MAXHEIGHT)
                    elif self.lexema.lower() == "min-height":
                        self.addToken(self.lexema,TT.MINHEIGHT)
                    elif self.lexema.lower() == "px":
                        self.addToken(self.lexema,TT.PX)
                    elif self.lexema.lower() == "em":
                        self.addToken(self.lexema,TT.EM)
                    elif self.lexema.lower() == "vh":
                        self.addToken(self.lexema,TT.VH)
                    elif self.lexema.lower() == "vw":
                        self.addToken(self.lexema,TT.VW)
                    elif self.lexema.lower() == "in":
                        self.addToken(self.lexema,TT.IN)
                    elif self.lexema.lower() == "cm":
                        self.addToken(self.lexema,TT.CM)
                    elif self.lexema.lower() == "mm":
                        self.addToken(self.lexema,TT.MM)
                    elif self.lexema.lower() == "pt":
                        self.addToken(self.lexema,TT.PT)
                    elif self.lexema.lower() == "pc":
                        self.addToken(self.lexema,TT.pc)
                    elif self.lexema.lower() == "relative":
                        self.addToken(self.lexema,TT.RELATIVE)
                    elif self.lexema.lower() == "inline-block":
                        self.addToken(self.lexema,TT.INLINEBLOCK)
                    elif self.lexema.lower() == "rgba":
                        self.addToken(self.lexema,TT.RGBA)
                    elif self.lexema.lower() == "url":
                        self.addToken(self.lexema,TT.URL)
                    elif self.lexema.lower() == "content":
                        self.addToken(self.lexema,TT.CONTENT)
                    else:
                        self.addToken(self.lexema,TT.ID)
            
            # Estado 4 - Cadenas 
            elif self.estado == 4:
                self.listadoEstados += " -> S4 " 
                if self.caracter == "$" and pos == len(self.entrada)-1:
                    self.addError(self.lexema,TE.ERERRONEA)
                elif self.caracter != "\"":
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 4
                    if self.caracter != "\n":
                        self.columna = 0
                        self.fila += 1
                        self.listadoEstados += "- " + "\\n"
                    else:
                        self.listadoEstados += "- " + self.caracter
                else:
                    self.addEstados(self.listadoEstados)
                    self.lexema += self.caracter
                    self.addToken(self.lexema,TT.CADENA)
            # Estado 5 - Identificadores y colores hexagecimales
            elif self.estado == 5:
                self.listadoEstados += " -> S5 " 
                if self.caracter.isalpha() or self.caracter.isnumeric():
                    self.listadoEstados += "- " + self.caracter
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 5
                else:
                    pos -= 1
                    self.addEstados(self.listadoEstados)
                    self.addToken(self.lexema,TT.ID)
            # Estado 6 - Comentarios 
            elif self.estado == 6:
                self.listadoEstados += " -> S6 " 
                if self.caracter == "*":
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 7
                    self.listadoEstados += "- " + self.caracter
            
            elif self.estado == 7:
                self.listadoEstados += " -> S7 " 
                if self.caracter == "$" and pos == len(self.entrada)-1:
                    self.addError(self.lexema,TE.ERERRONEA)
                    self.bandera = False
                elif self.caracter != "*":
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 7
                    if self.caracter == "\n":
                        self.columna = 0
                        self.fila += 1  
                        self.listadoEstados += "- \\n"
                    else: 
                        self.listadoEstados += "- " + self.caracter
                elif self.entrada[pos + 1] == "/":
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 8
                    self.listadoEstados += "- * -> S7" 
                else:
                    self.columna += 1
                    self.lexema += self.caracter
                    self.estado = 7
                    self.listadoEstados += "- " + self.caracter
                    
            elif self.estado == 8: 
                if self.caracter == "/":
                    if cont_Ruta == 1:
                        cont_Ruta += 1
                    elif cont_Ruta == 2:
                        self.Path = self.lexema.lstrip("/*PATHL:")
                        self.Path = self.Path.rstrip("*/")
                        self.Path = self.Path.strip()
                        cont_Ruta = 0
                    self.columna += 1
                    self.lexema += self.caracter    
                    self.addToken(self.lexema,TT.COMENTARIO)
                    self.listadoEstados += " - / -> S8 "
                    self.addEstados(self.listadoEstados)
            pos += 1      
            
    def addEstados(self,listaEstados):
        self.lista_estados.append(listaEstados)
        self.listadoEstados = "" 
                                          
    def addError(self, lexema,tipo):
        self.listadoEstados = "" 
        newError = Error(tipo,lexema,self.fila,self.columna)
        self.lista_errores.append(newError)
        self.estado = 0
        self.lexema = ""
        self.bandera = False
    
    def addToken(self, lexema, tipo):
        self.cadenaCorrecta += lexema
        newToken = Token(tipo,lexema,self.fila,self.columna)
        self.lista_tokens.append(newToken)
        self.estado = 0
        self.lexema = ""
    
    