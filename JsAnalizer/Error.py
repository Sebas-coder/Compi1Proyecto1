from enum import Enum

class Tipo(Enum):
    # Errores
    CARACTERINVALIDO = 0
    ERERRONEA = 1
    NINGUNO = 2
    
class Error:
    def __init__(self, tipo, valor, fila, columna ):
        self.tipoError = tipo
        self.lexema = valor
        self.fila = fila
        self.columna = columna