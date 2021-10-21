from datetime import date, time
from Enums import RoleList, Ranking
from typing import Any, List


# Importacion de clases
import EmployeeSchedule
import Payroll

# Creacion clase empleado
class Employee :

    # Constructor
    def __init__(self, __employeeId:int, __nameEmployee:str,  __salary:float, __role:RoleList, __ranking:List[Any], 
                __payrollId:int , __payNet:float , __percentDiscount:float , __percentAid:float, 
                __scheduleEmplId:int, __timeZoneEmpl:date, __availableEmpl:bool, __extraTime:float, __freeDays:date):


        # Datos de entrada
        self.schempls = []
        self.employeeId = __employeeId
        self.nameEmployee = __nameEmployee
        self.salary = __salary
        self.role = __role
        self.ranking = __ranking


        # COMPOSICIONES DE EMPLOYEE

        # PayRoll
        __payroll = Payroll()
        __payroll.payrollId = __payrollId
        __payroll.payNet = __payNet
        __payroll.percentDiscount = __percentDiscount
        __payroll.percentAid = __percentAid
        self.objpayr=[]
        self.objpayr [0] = __payroll


        # EmployeeSchedule
        __scheduleEmpl = EmployeeSchedule()
        __scheduleEmpl.scheduleEmplId = __scheduleEmplId
        __scheduleEmpl.timeZoneEmpl = __timeZoneEmpl
        __scheduleEmpl.availableEmpl = __availableEmpl
        __scheduleEmpl.extraTime = __extraTime
        __scheduleEmpl.freeDays = __freeDays
        self.objscheduleEmpl = []
        self.objscheduleEmpl [0] = __scheduleEmpl

# Metodos Getter and Setter
    # Getter Para EmployeeId
    def getEmployeeid(self):
        return self.employeeId


    # Getter and Setter Para nameEmployee
    def getNameEmployee(self):
        return self.nameEmployee

    def setNameEmployee(self, __nameEmployee):
        self.nameEmployee = __nameEmployee


    # Getter and Setter Para payroll
    def getPayRoll(self):
        return self.payroll

    def setPayRoll(self, __payroll):
        self.payroll = __payroll

    
    # Getter && Setter Para Role
    def getSalary(self):
        return self.salary

    def setSalary(self, __salary):
        self.salary = __salary


    # Getter && Setter Para Role
    def getRole(self):
        return self.role

    def setRole(self, __role):
        self.role = __role


    # Getter && Setter Para Ranking
    def getRanking(self):
        return self.ranking

    def setRanking(self, __ranking):
        self.ranking = __ranking


    # Getter && Setter Para ScheduleEmployee
    def getScheduleEmpl(self):
        return self.scheduleEmpl

    def setScheduleEmpl(self, __scheduleEmpl):
        self.scheduleEmpl = __scheduleEmpl
    # Metodos Getter and Setter END

    # Metodo ADD para scheduleempl
    def addScheduleEmpl(self, __scheduleEmplId:int, __timeZoneEmpl:date, __availableEmpl:bool):
        schempl = EmployeeSchedule(self, __scheduleEmplId, __timeZoneEmpl, __availableEmpl)
        self.schempls.append(schempl)

# EJEMPLO
# employee1 = Employee(3456, 'Oscar Ju', '3155555555', 25.000, RoleList.ADMINISTRATOR, Ranking.DOS, EmployeeSchedule)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'El ID del Empleado es: {employee1.getEmployeeid()}\n'
#         f'El nombre del Empleado es  {employee1.getNameEmployee()}\n'
#         f'El salario del Empleado es {employee1.getSalary()}\n'
#         f'El rol del Empleado es {employee1.getRole()}\n'
#         f'El ranking del Empleado es {employee1.getRanking()}')