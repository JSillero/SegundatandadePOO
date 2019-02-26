'''
Created on 21 feb. 2019

@author: d18sisaj
'''

class ClaseTiempo:
    def __init__(self,h,m,s):
        self.horas=h
        self.minutos=m
        self.segundos=s
        
        if(self.segundos>59): 
            self.minutos+=self.segundos//60
            self.segundos=self.segundos%60
       
    
        if(self.minutos>59):
            self.horas+=self.minutos//60
            self.minutos=self.minutos%60
      
        while(self.segundos<0):
            self.minutos-=1
            self.segundos+=60  
    
        while(self.minutos<0):
            self.horas-=1
            self.minutos+=60  
    
        if(self.horas<0):
            self.horas=0
            self.minutos=0
            self.segundos=0
            print("El tiempo total es negativo por lo que se ha reducido a 0h 0m 0s");
    
    def __str__(self):
        return(str(self.horas)+" h "+str(self.minutos)+" m "+str(self.segundos)+" s")
    '''
    metodo que sirve tanto para sumar como para restar, para restar simplemente emplee numeros negativos
    '''
    def suma(self, h,m,s):
        self.horas+=h
        self.minutos+=m
        self.segundos+=s
        
        if(self.segundos>59): 
            self.minutos+=self.segundos//60
            self.segundos=self.segundos%60
      
    
        if(self.minutos>59):
            self.horas+=self.minutos//60
            self.minutos=self.minutos%60
      
        while(self.segundos<0):
            self.minutos-=1;
            self.segundos+=60;   
    
        while(self.minutos<0):
            self.horas-=1;
            self.minutos+=60;
        
        if(self.horas<0):
            self.horas=0;
            self.minutos=0;
            self.segundos=0;
            print("El tiempo total es negativo por lo que se ha reducido a 0h 0m 0s");
        