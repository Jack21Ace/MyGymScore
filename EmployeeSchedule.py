from datetime import date, time

# Creacion clase
class EmployeeSchedule :

    # Constructor
    def __init__(self, __scheduleEmplId:int, __timeZoneEmpl:time, __availableEmpl:bool, __extraTime:int,
            __freeDays:int, __hourlyIntensity:int):

        # Datos de entrada
        self.__scheduleEmplId = __scheduleEmplId
        self.__timeZoneEmpl = __timeZoneEmpl
        self.__availableEmpl = __availableEmpl
        self.__extraTime = __extraTime
        self.__freeDays = __freeDays
        self.__hourlyIntensity = __hourlyIntensity

# Metodos STARTS
    # Getter para scheduleEmplId
    def getScheduleEmplId(self):
        return self.__scheduleEmplId


    # Getter && Setter para timeZoneEmpl
    def getTimeZoneEmpl(self):
        return self.__timeZoneEmpl

    def setTimeZoneEmpl(self, __timeZoneEmpl:time):
        self.__timeZoneEmpl = __timeZoneEmpl


    # Getter && Setter para availableEmpl
    def getAvailableEmpl(self):
        return self.__availableEmpl

    def setAvailableEmpl(self, __availableEmpl:bool):
        self.__availableEmpl = __availableEmpl

    # Getter && Setter para extraTime
    def getExtraTime(self):
        return self.__extraTime

    def setExtraTime(self, __extraTime:int):
        self.__extraTime = __extraTime


    # Getter && Setter para freedays
    def getFreeDays(self):
        return self.__freeDays

    def setFreeDays(self, __freeDays:int):
        self.__freeDays = __freeDays
    
    def getHourlyIntensity(self):
        return self.__hourlyIntensity

    def setHourlyIntensity(self, __hourlyIntensity:int):
        self.__hourlyIntensity = __hourlyIntensity


# Metodos ENDS
    def __str__(self):

        result = f"El codigo para el turno es {str(self.__scheduleEmplId)}\nDisponibilidad: {str(self.__availableEmpl)}\nSu horario: {str(self.__timeZoneEmpl)} AM\nCon una intensidad horaria de {str(self.__hourlyIntensity)} horas\ y cuenta con {str(self.__extraTime)} horas extras\nActualemnte tiene {str(self.__freeDays)} días libres"
        return result


# instancia del objeto
scheemployee1 = EmployeeSchedule(456, time(8,00), True, 2, 0, 8)
#print(scheemployee1.__str__())