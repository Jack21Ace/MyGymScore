from enum import Enum
from datetime import date, time
from Enums import RoleList, Ranking

# Importacion de clases
import EmployeeSchedule

# Creacion clase empleado
class Employee :

    # Constructor
    def __init__(self, __employeeId:int, __nameEmployee:str, __salary:float,
                __role:RoleList, __ranking:Ranking, __scheduleEmpl:EmployeeSchedule):

        # Datos de entrada
        self.schempl = []
        self.employeeId = __employeeId
        self.nameEmployee = __nameEmployee
        self.salary = __salary
        self.role = __role
        self.ranking = __ranking
        self.scheduleEmpl = __scheduleEmpl

# Metodos Getter and Setter
    # Getter Para EmployeeId
    def getEmployeeid(self):
        return self.employeeId

    # Getter and Setter Para nameEmployee
    def getNameEmployee(self):
        return self.nameEmployee

    def setNameEmployee(self, __nameEmployee):
        self.nameEmployee = __nameEmployee

    # Getter && Setter Para getSalary
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
    # Metodos Getter and Setter END

#    def getScheduleEmpl(self):
#        return self.ranking

#    def setScheduleEmpl(self, __scheduleEmpl):
#        self.scheduleEmpl = __scheduleEmpl

#    def addScheduleEmpl(self, __scheduleEmplId:int, __timeZoneEmpl:date, __availableEmpl:bool):
#        scheduleEmpl = __scheduleEmplId, __timeZoneEmpl, __availableEmpl
#        scheduleEmpl in self.schempl

# EJEMPLO

employee1 = Employee(3456, 'Oscar Ju', 25.000, RoleList.ADMINISTRATOR, Ranking.DOS, EmployeeSchedule)


print("==========//==========//==========//==========//==========//==========//==========")
print(f'El ID del Empleado es: {employee1.getEmployeeid()}\n'
        f'El nombre del Empleado es  {employee1.getNameEmployee()}\n'
        f'El salario del Empleado es {employee1.getSalary()}\n'
        f'El rol del Empleado es {employee1.getRole()}\n'
        f'El ranking del Empleado es {employee1.getRanking()}')

#print(f'El Calendario del empleado es {employee1.getScheduleEmpl}\n')
# print(f'El Calendario del empleado es {employee1.addScheduleEmpl}\n')

# NOTAS :

# Mirar bien que los nombres de los atributos concuerden con
# sus respectivos metodos y parametros de entrada


# Pendiente por añadir el metodo addOffer()

# Preguntar por la lista Ranking, lista scheduleempl

# hola