from datetime import date, time
from Enums import Role, Ranking
from typing import List


# Importacion de clases
from EmployeeSchedule import EmployeeSchedule
from Payroll import Payroll

# Creacion clase empleado
class Employee :

    # Constructor
    def __init__(self, __employeeId:int, __nameEmployee:str, __phoneEmployee:str, 
                __salary:float, __role:Role, __ranking:Ranking):

        # Datos de entrada
        self.__employeeId = __employeeId
        self.__nameEmployee = __nameEmployee
        self.__phoneEmployee = __phoneEmployee
        self.__salary = __salary
        self.__role = __role
        self.__payroll = Payroll(10, 900000, 0.12 , 0.25)         # Composición Payroll()
        self.__ranking = __ranking
        self.__listRanking:List[Ranking] = []
        self.__scheduleEmpl =  EmployeeSchedule(456, time(8,00), True, 2, 0, 8) # Composición EmployeeSchedule()
        self.__listScheduleEmpl:List[EmployeeSchedule] = []
   
# Metodos Getter and Setter
    # Getter Para EmployeeId
    def getEmployeeid(self):
        return self.__employeeId


    # Getter and Setter Para nameEmployee
    def getNameEmployee(self):
        return self.__nameEmployee

    def setNameEmployee(self, __nameEmployee:str):
        self.__nameEmployee = __nameEmployee


    # Getter and Setter Para phoneEmployee
    def getPhoneEmployee(self):
        return self.__phoneEmployee

    def setPhoneEmployee(self, __phoneEmployee:str):
        self.__phoneEmployee = __phoneEmployee


    # Getter && Setter Para Salary
    def getSalary(self):
        return self.__salary

    def setSalary(self, __salary:float):
        self.__salary = __salary


    # Getter && Setter Para Role
    def getRole(self):
        return self.__role

    def setRole(self, __role:Role):
        self.__role = __role


    # Getter && Setter Para Ranking
    def getRanking(self):
        return self.__ranking

    def setRanking(self, __ranking:Ranking):
        self.__ranking = __ranking


    # Getter && Setter Para listRanking
    def getListRanking(self):
        return self.__listRanking

    def setListRanking(self, __listRanking:List[Ranking]):
        self.__listRanking = __listRanking


    # Getter and Setter Para payroll
    def getPayRoll(self):
        return self.__payroll
 
    def setPayRoll(self, __payroll:Payroll):
        self.__payroll = __payroll
 

    # Getter && Setter Para ScheduleEmployee
    def getScheduleEmpl(self):
        return self.__scheduleEmpl

    def setScheduleEmpl(self, __scheduleEmpl:EmployeeSchedule):
        self.__scheduleEmpl =  __scheduleEmpl

    # Getter && Setter Para listScheduleEmpl
    def getListScheduleEmpl(self):
        return self.__listScheduleEmpl

    def setListScheduleEmpl(self, __listScheduleEmpl:List[EmployeeSchedule]):
        self.__listScheduleEmpl = __listScheduleEmpl

# Metodos Getter and Setter END

# Metodo ADD para scheduleempl
    def addScheduleEmpl(self, __scheduleEmplId:int, __timeZoneEmpl:date, __availableEmpl:bool):
        __listScheduleEmpl = EmployeeSchedule(self, __scheduleEmplId, __timeZoneEmpl, __availableEmpl)
        self.__listScheduleEmpl.append(__listScheduleEmpl)
        return self.__listScheduleEmpl
           
    def __str__(self):
        cadena = f'El ID del empleado es: {str(self.__employeeId)}\nEl nombre del empleado es:  {str(self.__nameEmployee)}\nEl telefono de {str(self.__nameEmployee)} es: {str(self.__phoneEmployee)}\nEl salario de {str(self.__nameEmployee)} es: {str(self.__salary)}\nEl rol de {str(self.__nameEmployee)} es: {str(self.__role.value)}\nEl ranking de {str(self.__nameEmployee)} es: {str(self.__ranking.value)}\nEl horario de {str(self.__nameEmployee)} es {str(self.__scheduleEmpl.getTimeZoneEmpl())}\nEl total a pagar a {str(self.__nameEmployee)} es: {str(self.__payroll.totalPagar())}'
        return cadena
        
employee1 = Employee(2375, 'Oscar Andres', '317 8613343', 250000, Role.ADMINISTRATOR, Ranking.DOS)
