# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:44:56 2021

@author: Juan Camilo
"""

from datetime import date

#Creación de la clase offer
class Offer:
    # Declaración del constructor
    def __init__(self, __eventCode:int, __name:str, __start:date, __end:date, __description:str, __available:bool):
        self.__eventCode = __eventCode
        self.__name = __name
        self.__start = __start
        self.__end = __end
        self.__description = __description
        self.__available = __available

    

# START METHODS
    # Getter para eventCode
    def getEventCode(self):
        return self.__eventCode

    # Getter && Setter para name
    def getName(self):
        return self.__name

    def setName(self, __name:str):
        self.__name = __name

    # Getter && Setter para start
    def getStart (self):
        return self.__start

    def setStart(self, __start:date):
        self.__start = __start

    # Getter && Setter para end
    def getEnd (self):
        return self.__end

    def setEnd(self, __end:date):
        self.__end = __end

    # Getter && Setter para description
    def getDescription (self):
        return self.__description

    def setDescription(self, __description:str):
        self.__description = __description

    # Getter && Setter para available
    def getAvailable (self):
        return self.__available

    def setAvailable(self, __available:bool):
        self.__available = __available

# offer1 = Offer(1232, 'Zamba', date(2021, 11, 13), date(2021, 11, 14), 'baile', True)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'Actividad {offer1.getName()}\n'
#     f'Su código es {offer1.getEventCode()}\n'
#     f'La fecha de inscripción {offer1.getStart()}\n'
#     f'Plazo hasta {offer1.getEnd()}\n'
#     f'Descripción del evento {offer1.getDescription()}\n'
#     f'Disponibilidad {offer1.getAvailable()}')