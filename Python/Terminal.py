'''
Created on 12 feb. 2019

@author: d18sisaj
'''

class Terminal:
    def __init__(self,n):
        self.__numero=n
        self._tiempo=0
        
    def __str__(self):
        return("Nº "+str(self.__numero)+" - "+str(self._tiempo)+" s de conversación.")
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def tiempo(self):
        return self._tiempo
    
    def llamada(self, Terminal,t):
        self._tiempo+=t
        Terminal._tiempo+=t