#import BodyZone

#Creación de la clase Routine
from typing import Any, Counter
import BodyZone


class Routine:
    # Declaración del constructor
    def __init__(self, __routineId:int, __name:str, __series:int, __count:int, __weight:float, __createdBy:str, __bodyZone:BodyZone):
        # Datos de entrada
        self.routineId = __routineId
        self.name = __name
        self.series = __series
        self.count = __count
        self.weight = __weight
        self.createdBy = __createdBy

    def getRoutineId(self):
        return self.routineId

    def getName(self):
        return self.name

    def setName(self, __name):
        self.name = __name

    def getSeries(self):
        return self.series

    def setSeries(self, __series):
        self.series = __series

    def getCount(self):
        return self.count

    def setCount(self, __count):
        self.count = __count

    def getWeight(self):
        return self.weight

    def setWeight(self, __weight):
        self.weight = __weight

    def getCreatedBy(self):
        return self.getCreatedBy

    def setCreatedBy(self, __createdBy):
        self.createdBy = __createdBy

routine1 = Routine(1, 'Tren Superior', 4, 10, 20.5, 'Donald', BodyZone)
print("==========//==========//==========//==========//==========//==========//==========")
print(f'Hola\nSu rutina para hoy es: {routine1.getName()}, esperamos que te diviertas')

