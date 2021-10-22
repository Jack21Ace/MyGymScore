from datetime import date
from Routine import Routine
from typing import List

class RoutineHistory:

# Declaración del constructor

    
    routines:List[Routine]=[]

    def addRoutine(self, __routineId:int, __name:str, __serie:float, __count:float, __weight:float, __createdBy:str, __timer:date):
        routine = Routine(self, __routineId, __name, __serie, __count, __weight, __createdBy)
        self.routines.append(routine)

    def searchRoutine(searchFor:List[Routine]):
        pass
