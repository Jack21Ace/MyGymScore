#import BodyZone

#Creación de la clase Routine
from typing import Any, Counter, List
from BodyZone import BodyZone
from datetime import time
from Employee import Employee
from Enums import Conditioning, LowerBody, UpperBody, Role, Ranking


class Routine:
    # Declaración del constructor
    def __init__(self, __routineId:int, __series:int, __count:int, __weight:float, __createdBy:Employee, __timer:time):

        # Datos de entrada
        self.__routineId = __routineId
        self.__series = __series
        self.__count = __count
        self.__weight = __weight
        self.__createdBy = __createdBy
        self.__timer = __timer
        self.__routineHistory:List = []
        self.__bodyZone = BodyZone(UpperBody.ABDOMEN, LowerBody.QUADRICEPS_FEMORIS, Conditioning.RUN) # Composicion de BodyZone

    def getRoutineId(self):
        return self.__routineId
  
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

    def setCreatedBy(self, __createdBy:Employee):
        self.__createdBy = __createdBy

    def getTimer(self): 
        return self.__timer

    def setTimer(self, __timer:time):
        self.__timer = __timer

    def getRoutineHistory(self):
        return self.__routineHistory

    def setRoutineHistory(self, __routineHistory:List): 
        self.__routineHistory = __routineHistory

    def getBodyZone(self):
        return self.__bodyZone

    def __str__(self):
        cadena = f"El Id de la rutina es: {str(self.__routineId)}\nVa a hacer {str(self.__series)} series de {str(self.__count)}\nEl peso es: {str(self.__weight)} kilos\nComienza a las  {str(self.__timer)}\nLa zona de trabajo del cuerpo para esta rutina va a ser: {str(self.__bodyZone.getLowerBody().value)}\nCreado por: {str(self.__createdBy)}"
        return cadena 
