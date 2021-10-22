from datetime import date

# Creacion clase
class EmployeeSchedule :

    # Constructor
    def __init__(self, __scheduleEmplId:int, __timeZoneEmpl:date, __availableEmpl:bool, __extraTime:float, 
            __freeDays:date):

        # Datos de entrada
        self.__scheduleEmplId = __scheduleEmplId
        self.__timeZoneEmpl = __timeZoneEmpl
        self.__availableEmpl = __availableEmpl
        self.__extraTime = __extraTime
        self.__freeDays = __freeDays

# Metodos STARTS
    # Getter para scheduleEmplId
    def getScheduleEmplId(self):
        return self.__scheduleEmplId


    # Getter && Setter para timeZoneEmpl
    def getTimeZoneEmpl(self):
        return self.__timeZoneEmpl

    def setTimeZoneEmpl(self, __timeZoneEmpl):
        self.__timeZoneEmpl = __timeZoneEmpl


    # Getter && Setter para availableEmpl
    def getAvailableEmpl(self):
        return self.__availableEmpl

    def setAvailableEmpl(self, __availableEmpl):
        self.__availableEmpl = __availableEmpl

    
    # Getter && Setter para extraTime
    def getExtraTime(self):
        return self.__extraTime

    def setExtraTime(self, __extraTime):
        self.__extraTime = __extraTime


    # Getter && Setter para freedays
    def getFreeDays(self):
        return self.__freeDays

    def setFreeDays(self, __freeDays):
        self.__freeDays = __freeDays
# Metodos ENDS



# instancia del objeto
# scheemployee1 = EmployeeSchedule(897644, time(13,30,5), True)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'El ID del Calendario del Empleado es: {scheemployee1.getScheduleEmplId()}\n'
#         f'El Horario del Empleado es  {scheemployee1.getTimeZoneEmpl()}\n'
#         f'La disponibilidad del empleado es {scheemployee1.getAvailableEmpl()}')

