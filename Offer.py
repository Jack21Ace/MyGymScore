# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:52:43 2021

@author: Juan Camilo
"""

from datetime import date

#Creación de la clase offer
class Offer:
     # Declaración del constructor
    def __init__(self, __eventCode:int, __name:str, __start:date, __end:date, __description:str, __available:bool):
         self.eventCode = __eventCode
         self.name = __name
         self.start = __start
         self.end = __end
         self.description = __description
         self.available = __available
         
    def getEvent(self):
        return self.eventCode
    def getName(self):
        return self.name
    def setName(self, __name):
        self.name = __name
    def getStart (self):
        return self.start
    def setStart(self, __start):
        self.start = __start
    def getEnd (self):
        return self.end
    def setEnd(self, __end):
        self.end = __end
    def getDescription (self):
        return self.description
    def setDescription(self, __description):
        self.description = __description
    def getAvailable (self):
        return self.available
    def setAvailable(self, __available):
        self.available = __available
    
offer1 = Offer(1232, 'Zamba', date(2021, 11, 13), date(2021, 11, 14), 'baile', True)
        
print(f'Actividad {offer1.getName()}\nSu código es {offer1.getEvent()}\nLa fecha de inscripción {offer1.getStart()}\nPlazo hasta {offer1.getEnd()}\nDescripción del evento {offer1.getDescription()}\nDisponibilidad {offer1.getAvailable()}')


        