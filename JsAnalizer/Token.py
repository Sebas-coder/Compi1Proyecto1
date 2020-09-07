from enum import Enum


class Tipo(Enum):
    # Simbolos del Lenguaje
    IGUAL = 1
    ASTERISCO = 2
    PARENDER = 3
    PARENIZQ = 4
    MAS = 5
    MENOS = 6
    LLAVEIZQ = 7
    LLAVEDER = 8
    DOSPUNTOS = 9
    PUNTO = 10
    
    DIAGONAL = 12
    
    IGUALDAD = 13
    
    DIFERENTEDE = 14
    MAYORQUE = 15
    MENORQUE = 16
    
    MAYORIGUAL = 17
    MENORIGUAL = 18
    
    CONJUNCION = 19
    DISYUNCION = 20
    
    ADMIRACIONIZQ = 21
    
    # Palabras reservadas
    INT = 22
    STRING = 23
    CHAR = 24
    BOOLEAN = 25
    TYPE = 26
    IF = 27
    ELSE = 28
    FOR  = 29
    WHILE = 30
    DO = 31
    CONTINUE = 32
    BREAK = 33
    RETURN = 34
    TRUE = 35
    FALSE = 36
    FUNCTION = 37
    CONSTRUCTOR = 38
    CLASS = 39
    MATH = 40
    POW = 41
    PATH = 42
    THIS = 43
    
    # Expresines regulares
    ID = 44
    NUMERO = 45
    COMENTUNI = 46
    COMENTMUL = 47
    PUNTOYCOMA = 48
    COMA = 49
    CARACTER = 50
    CADENA = 51
    
class Token:
    def __init__(self, tipo, lexema,fila, columna):
        self.tipoToken = tipo
        self.lexema = lexema
        self.fila = fila 
        self.columna = columna