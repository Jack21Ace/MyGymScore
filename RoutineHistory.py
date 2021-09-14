from Routine import Routine


class RoutineHistory:

# Declaración del constructor

    def __init__(self):
        self.routineList = []

    def addRoutine(self, __routineId:int, __name:str, __serie:float, __count:float, __weight:float, __createdBy:str):
        routine = Routine(self, __routineId, __name, __serie, __count, __weight, __createdBy)
        self.routineList.append(routine)
