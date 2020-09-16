from enum import Enum

class Tipo(Enum):
    # Simbolos
    MENORQUE = 1
    MAYORQUE = 2
    DIAGONAL = 3
    IGUAL = 4
    COMILLAS = 5
    DOSPUNTOS = 6
    
    # Palabras reservadas
    HTML = 7 
    HEAD = 8
    TITLE = 9
    BODY = 10
    H = 11
    P = 12
    BR = 13
    IMG = 14
    SRC = 15
    A = 16 
    OL = 17 
    UL = 18
    STYLE = 19
    TABLE = 20
    TH = 21 
    TR = 22
    TD = 23
    CAPTION = 24
    COLGROUP = 25
    COL = 26
    THEAD = 27
    TBODY = 28
    TFOOT = 29
    
    # Expresiones regulares
    VALOR = 30
    VINCULOIMAGEN = 31
    HIPERVINCULO = 32
    CADENA = 33
    SINREGISTRAR = 34
    LI = 35
    SIMBOLO = 36
    COMENTARIO = 37
    
class Token:
    tipoToken = Tipo.SINREGISTRAR
    lexema = ""
    def __init__(self, tipo, lexema ):
        self.tipoToken = tipo
        self.lexema = lexema
