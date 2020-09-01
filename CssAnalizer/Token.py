from enum import Enum


class Tipo(Enum):
    # Simbolos del Lenguaje
    LLAVEIZQ = 1 
    LLAVEDER = 2
    DOSPUNTOS = 3
    PUNTOYCOMA = 4
    COMA = 5
    HASH = 6 
    PARENIZQ = 54
    PARENDER = 55
    
    # Palabras reservadas
    COLOR = 7
    BACKGRCOLOR = 8
    BACKGRIMAGE = 9
    BORDER = 10
    OPACITY = 11
    BACKGROUND = 12
    TEXTALING = 13
    FONTFAMILY = 14 
    FONTSTYLE = 15
    FONTWEIGHT = 16
    FONTSIZE = 17
    FONT = 18
    PADDLEFT = 19
    PADDRIGHT = 20
    PADDBOTTOM = 21
    PADDTOP = 22
    PADDING = 23
    DISPLAY = 24
    LINEHEIGHT = 25
    WINDTH = 26 
    HEIGHT = 27 
    MARGTOP = 28 
    MARGRIGHT = 29
    MARGBOTTOM = 30
    MARGLEFT = 31 
    MARGING = 32
    BORDERSTYLE = 33
    POSITION = 34 
    BOTTOM = 35
    TOP = 36
    RIGHT = 37
    LEFT = 38
    FLOAT = 39
    CLEAR = 40
    MAXWIGTH = 41
    MINWIGTH = 42
    MAXHEIGHT = 43
    MINHEIGHT = 44
    
    # Unidades de madida
    PX = 45
    EM = 46
    VH = 47
    VW = 48
    IN = 49
    CM = 50
    MM = 51
    PT = 52
    PC = 53
    
    # OTRAS PALABRAS RESERVADAS 56
    URL = 56
    RGBA = 57
    
    # IDENTIFICADORES
    RELATIVE = 58
    INLINEBLOCK = 59
    PORCENTAJE = 60
    
    # Expresiones regulares
    ID = 61
    NUMERO = 62
    HEXACOLOR = 63
    CADENA = 64
    
class Token:
    tipoToken = Tipo.SINREGISTRAR
    lexema = ""
    def __init__(self, tipo, lexema ):
        self.tipoToken = tipo
        self.lexema = lexema