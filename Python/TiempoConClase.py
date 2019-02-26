'''
Created on 25 feb. 2019
Implementacion del ejercicio tiempo, con clases nativas de python
@author: d18sisaj
'''
import datetime
'''timedelta es necesario para hacer operaciones'''
from datetime import timedelta

tiempo=datetime.time(1,2,4)
print(tiempo)
tiempo=tiempo+timedelta(hours=20)
print(tiempo)
