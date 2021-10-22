#import BodyZone

#Creación de la clase Routine
from typing import Any, Counter
import BodyZone
from datetime import datetime


class Routine:
    # Declaración del constructor
    def __init__(self, __routineId:int, __name:str, __series:int, __count:int, __weight:float, __createdBy:str, __bodyZone:BodyZone, __timer:datetime):
        # Datos de entrada
        self.__routineId = __routineId
        self.__name = __name
        self.__series = __series
        self.__count = __count
        self.__weight = __weight
        self.__createdBy = __createdBy
        self.__timer = __timer

    def getRoutineId(self):
        return self.__routineId

    def getName(self):
        return self.__name

    def setName(self, __name:str):
        self.__name = __name


    # revisar GET
    def getBodyZone(self):
        return self.bodyZone
  
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

    def getBodyZone(self):
        return self.__bodyZone

    def setBodyZone(self, __bodyZone:BodyZone):
        self.__bodyZone = __bodyZone
        

    def getTimer(self):
        return self.__timer

    def setTimer(self, __timer:datetime):
        self.__timer = __timer

# routine1 = Routine(1, 'Tren Superior', 4, 10, 20.5, 'Donald', BodyZone)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'Hola\nSu rutina para hoy es: {routine1.getName()}, esperamos que te diviertas')

