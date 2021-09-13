from enum import Enum

from datetime import date, time
# Creacion clase 
class EmployeeSchedule :

    # Constructor
    def __init__(self, __scheduleEmplId:int, __timeZoneEmpl:date,
                __availableEmpl:bool):

        # Datos de entrada 
        self.scheduleEmplId = __scheduleEmplId
        self.timeZoneEmpl = __timeZoneEmpl
        self.availableEmpl = __availableEmpl
 
    # Metodos

    # get
    def getScheduleEmplId(self):
        return self.scheduleEmplId
    
    def getTimeZoneEmpl(self):
        return self.timeZoneEmpl

    def getAvailableEmpl(self):
        return self.availableEmpl

    # set

    def setTimeZoneEmpl(self, __scheduleEmplId):
        self.scheduleEmplId = __scheduleEmplId
    
    def setAvailableEmpl(self, __availableEmpl):
        self.availableEmpl = __availableEmpl


# ejemplo

scheemployee1 = EmployeeSchedule(897644, time(13,30,5), True)

print(f'El ID del Calendario del Empleado es: {scheemployee1.getScheduleEmplId()}\n') 
print(f'El Horario del Empleado es  {scheemployee1.getTimeZoneEmpl()}\n')
print(f'La disponibilidad del empleado es {scheemployee1.getAvailableEmpl()}\n')
   