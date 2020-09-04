from enum import Enum


class Tipo(Enum):
    # Errores
    CARACTERINVALIDO = 0
    ERERRONEA = 1
    NINGUNO = 2
    
class Error:
    tipoError = Tipo.NINGUNO
    lexema = ""
    def __init__(self, tipo, valor ):
        self.tipoError = tipo
        self.lexema = valor