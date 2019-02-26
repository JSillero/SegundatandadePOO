'''
Created on 15 feb. 2019
Esta es la prueba de terminal y movil
@author: d18sisaj
'''
from Movil import Movil
movil1=Movil( "123456789", "rata")
movil2=Movil( "123456785", "mono")
movil3=Movil( "198765432", "bison")
movil1.llamada(movil3, 560)
movil2.llamada(movil3, 360)
movil3.llamada(movil1, 660 )
print(movil1)
print(movil2)
print(movil3)