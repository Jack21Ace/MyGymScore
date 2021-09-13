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

# Metodos STARTS
    # Getter para scheduleEmplId
    def getScheduleEmplId(self):
        return self.scheduleEmplId

    # Getter && Setter para timeZoneEmpl
    def getTimeZoneEmpl(self):
        return self.timeZoneEmpl

    def setTimeZoneEmpl(self, __timeZoneEmpl):
        self.timeZoneEmpl = __timeZoneEmpl

    # Getter && Setter para availableEmpl
    def getAvailableEmpl(self):
        return self.availableEmpl

    def setAvailableEmpl(self, __availableEmpl):
        self.availableEmpl = __availableEmpl
# Metodos ENDS

# instancia del objeto
scheemployee1 = EmployeeSchedule(897644, time(13,30,5), True)
print("==========//==========//==========//==========//==========//==========//==========")
print(f'El ID del Calendario del Empleado es: {scheemployee1.getScheduleEmplId()}\n'
        f'El Horario del Empleado es  {scheemployee1.getTimeZoneEmpl()}\n'
        f'La disponibilidad del empleado es {scheemployee1.getAvailableEmpl()}')

