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
        
    
    
    def parea(self, tipoToken):
        # Si esta incorrecto
        if self.bandera:
            if self.indice < self.lista_size:
                self.indice += 1
                self.pre_analisis = self.lista_tokens[self.indice]
            else:
                print("Llego al token final")
        # Si correcto
        else: 
            # Coincide el token
            if self.pre_analisis == tipoToken:
                if self.indice < self.lista_size:
                    self.indice += 1
                    self.pre_analisis = self.lista_tokens[self.indice]
            # No coincide error
            else: 
                #Se detecta error
                self.bandera = True