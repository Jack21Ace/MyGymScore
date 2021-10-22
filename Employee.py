from datetime import date
from Enums import RoleList, Ranking
from typing import List


# Importacion de clases
from EmployeeSchedule import EmployeeSchedule
from Payroll import Payroll

# Creacion clase empleado
class Employee :

    # Constructor
    def __init__(self, __employeeId:int, __nameEmployee:str,  __salary:float, __role:RoleList, __payRoll:Payroll,
            __ranking:List[Ranking], __listRanking:List[Ranking], __scheduleEmpl:EmployeeSchedule, __listScheduleEmpl:List[EmployeeSchedule]):


        # Datos de entrada
        self.__employeeId = __employeeId
        self.__nameEmployee = __nameEmployee
        self.__salary = __salary
        self.__role = __role
        self.__payRoll = __payRoll

        self.__ranking = __ranking
        self.__listRanking = __listRanking
        self.__listRanking:List[Ranking] = []

        self.__scheduleEmpl = __scheduleEmpl
        self.__listScheduleEmpl = __listScheduleEmpl
        self.__listScheduleEmpl:List[EmployeeSchedule] = []


# Metodos Getter and Setter
    # Getter Para EmployeeId
    def getEmployeeid(self):
        return self.__employeeId


    # Getter and Setter Para nameEmployee
    def getNameEmployee(self):
        return self.__nameEmployee

    def setNameEmployee(self, __nameEmployee):
        self.__nameEmployee = __nameEmployee

    
    # Getter && Setter Para Salary
    def getSalary(self):
        return self.__salary

    def setSalary(self, __salary):
        self.__salary = __salary


    # Getter && Setter Para Role
    def getRole(self):
        return self.__role

    def setRole(self, __role):
        self.__role = __role


    # Getter and Setter Para payroll
    def getPayRoll(self):
        return self.__payroll

    def setPayRoll(self, __payroll):
        self.__payroll = __payroll


    # Getter && Setter Para Ranking
    def getRanking(self):
        return self.__ranking

    def setRanking(self, __ranking):
        self.__ranking = __ranking


    # Getter && Setter Para listRanking
    def getListRanking(self):
        return self.__listRanking

    def setListRanking(self, __listRanking):
        self.__listRanking = __listRanking


    # Getter && Setter Para ScheduleEmployee
    def getScheduleEmpl(self):
        return self.__scheduleEmpl

    def setScheduleEmpl(self, __scheduleEmpl):
        self.__scheduleEmpl = __scheduleEmpl

    
    # Getter && Setter Para listScheduleEmpl
    def getListScheduleEmpl(self):
        return self.__listScheduleEmpl

    def setListScheduleEmpl(self, __listScheduleEmpl):
        self.__listScheduleEmpl = __listScheduleEmpl

# Metodos Getter and Setter END


# Metodo ADD para scheduleempl
    def addScheduleEmpl(self, __scheduleEmplId:int, __timeZoneEmpl:date, __availableEmpl:bool):
        __listScheduleEmpl = EmployeeSchedule(self, __scheduleEmplId, __timeZoneEmpl, __availableEmpl)
        self.__listScheduleEmpl.append(__listScheduleEmpl)

# EJEMPLO
# employee1 = Employee(3456, 'Oscar Ju', '3155555555', 25.000, RoleList.ADMINISTRATOR, Ranking.DOS, EmployeeSchedule)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'El ID del Empleado es: {employee1.getEmployeeid()}\n'
#         f'El nombre del Empleado es  {employee1.getNameEmployee()}\n'
#         f'El salario del Empleado es {employee1.getSalary()}\n'
#         f'El rol del Empleado es {employee1.getRole()}\n'
#         f'El ranking del Empleado es {employee1.getRanking()}')