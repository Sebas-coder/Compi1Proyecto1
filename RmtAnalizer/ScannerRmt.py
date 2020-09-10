from JsAnalizer.Token import Token
from JsAnalizer.Token import Tipo as TT

class Scanner:
    indice = 0
    lista_tokens = list()
    bandera = False
    lista_size = 0
    pre_analisis = TT.NINGUNO   
    
    def __init__(self):  
        print("INICIO DE ANALISIS JS")
        
    def inicio(self,lista):
        self.lista_tokens = lista
        self.lista_size = len(self.lista_tokens) - 1
        self.pre_analisis = self.lista_tokens[self.indice]
        
    def E(self):
        self.T() 
        self.EP()
        
    def EP(self):
        # +
        if self.pre_analisis == TT.MAS:
            self.parea(TT.MAS)
            self.T()
            self.EP()
        # |*
        elif self.pre_analisis == TT.MENOS:
            self.parea(TT.MENOS)
            self.T()
            self.EP()
        # |epcilon
        else:
            return
    
    def T(self):
        self.F()
        self.TP()
        
    def TP(self):
        # *
        if self.pre_analisis == TT.ASTERISCO:
            self.parea(TT.ASTERISCO)
            self.F()
            self.TP()
        # |/
        elif self.pre_analisis == TT.DIAGONAL:
            self.parea(TT.DIAGONAL)
            self.F()
            self.TP()
        # |epcilon
        else:
            return
    
    def F(self):
        # Numero
        if self.pre_analisis == TT.NUMERO:
            self.parea(TT.NUMERO)
        # |ID
        elif self.pre_analisis == TT.ID:
            self.parea(TT.ID)
        # |(
        elif self.pre_analisis == TT.PARENIZQ:
            self.parea(TT.PARENIZQ)
            self.E()
            self.parea(TT.PARENDER)
    
    def parea(self, tipoToken):
        # Si esta incorrecto
        if self.bandera:
            # Solo itera hasta la ultima posicion
            if self.indice < self.lista_size:
                self.indice += 1
                self.pre_analisis = self.lista_tokens[self.indice]
        # Si correcto
        else: 
            # Coincide el token
            if self.pre_analisis == tipoToken:
                # Coincide y pasa al siguiente
                if self.indice < self.lista_size:
                    self.indice += 1
                    self.pre_analisis = self.lista_tokens[self.indice]
            # No coincide error
            else: 
                #Se detecta error y pasa al siguiente
                self.bandera = True
                if self.indice < self.lista_size:
                    self.indice += 1
                    self.pre_analisis = self.lista_tokens[self.indice]
        