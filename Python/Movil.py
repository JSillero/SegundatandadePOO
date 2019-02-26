'''
Created on 12 feb. 2019

@author: d18sisaj
'''
from Terminal import Terminal
'''
La tarifa solo puede ser "mono" "rata" o "bisonte"
'''
class Movil(Terminal):
    def __init__(self,numero,tarifa):
        super().__init__(numero)
        self.__tar=tarifa 
        self.__deuda=0.0000001
        
    def __str__(self):
        return("Nº "+str(self.numero)+" - "+str(self.tiempo)+" s de conversación. - tarifados  {0:.2f} euros".format(self.__deuda))
        
    def llamada(self, Terminal, t):
        self._tiempo+=t
        Terminal._tiempo+=t
        if(self.__tar=="rata"):
            self.__deuda+=((0.06)/60*t)
        elif(self.__tar=="mono"):
            self.__deuda+=((0.12)/60*t)
        else:
            self.__deuda+=((0.30)/60*t)