#import BodyZone

#Creación de la clase Routine
from typing import Any, Counter
from BodyZone import BodyZone
from datetime import time

from Enums import Conditioning, LowerBody, UpperBody


class Routine:
    # Declaración del constructor
    def __init__(self, __routineId:int, __name:str, __series:int, __count:int, __weight:float, __createdBy:str, __timer:time):
        # Datos de entrada
        self.__routineId = __routineId
        self.__name = __name
        self.__series = __series
        self.__count = __count
        self.__weight = __weight
        self.__createdBy = __createdBy
        self.__timer = __timer
        self.__bodyZone = []

    def getRoutineId(self):
        return self.__routineId

    def getName(self):
        return self.__name

    def setName(self, __name:str):
        self.__name = __name
  
    def getSeries(self):
        return self.__series

    def setSeries(self, __series:int):
        self.__series = __series

    def getCount(self):
        return self.__count

    def setCount(self, __count:int):
        self.__count = __count

    def getWeight(self):
        return self.__weight

    def setWeight(self, __weight:float):
        self.__weight = __weight

    def getCreatedBy(self):
        return self.__createdBy

    def setCreatedBy(self, __createdBy:str):
        self.__createdBy = __createdBy

    # def addBodyZone(self, bodyZone):
    #     self.__bodyZone.append(bodyZone)

    # def totalBodyZone(self):
    #     result:str = ""
    #     for bodyZone in self.__bodyZone:
    #         result += bodyZone.__upperBody
    #     return result

    def getTimer(self):
        return self.__timer

    def setTimer(self, __timer:time):
        self.__timer = __timer

    def __str__(self):
        cadena = f"Hola {str(self.__name)}"
        return cadena 

routine1 = Routine(1, "Donald", 4,12,20,"Instructor",time(8,12))
print("==========//==========//==========//==========//==========//==========//==========")
#routine1.addBodyZone(BodyZone(UpperBody.TRAPEZE,LowerBody.HAMSTRINGS,Conditioning.SPINING_BIKE))
print(routine1.__str__()) 
print(f"Su rutina para hoy sera: ") 
#print(f'Hola {routine1.getName()}\nSu rutina para hoy es: {routine1.getBodyZone().value} {routine1.getSeries()} Series de ')
 