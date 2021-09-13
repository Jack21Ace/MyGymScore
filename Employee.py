from enum import Enum
from datetime import date, time
from Enums import RoleList, Ranking

# Importacion de clases
import EmployeeSchedule

# Importacion de las claes pendientes
#import Offer

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
    
    # Metodos 
    def getEmployeeid(self): 
        return self.employeeId

    def getNameEmployee(self):
        return self.nameEmployee

    def getSalary(self):
        return self.salary

    def getRole(self):
        return self.role
    
    def getRanking(self):
        return self.ranking
    
    def setEmployeeid(self, __employeeId):
        self.employeeId = __employeeId

    def setNameEmployee(self, __nameEmployee):
        self.nameEmployee = __nameEmployee

    def setSalary(self, __salary):
        self.salary = __salary
    
    def setRole(self, __role):
        self.role = __role
    
    def setRanking(self, __ranking):
        self.ranking = __ranking

#    def getScheduleEmpl(self):
#        return self.ranking

#    def setScheduleEmpl(self, __scheduleEmpl):
#        self.scheduleEmpl = __scheduleEmpl

#    def addScheduleEmpl(self, __scheduleEmplId:int, __timeZoneEmpl:date, __availableEmpl:bool):
#        scheduleEmpl = __scheduleEmplId, __timeZoneEmpl, __availableEmpl                
#        scheduleEmpl in self.schempl
         


        # EJEMPLO 
          
employee1 = Employee(3456, 'Oscar Ju', 25.000, RoleList.ADMINISTRATOR, Ranking.DOS, EmployeeSchedule)
 
  
print("==========//==========//==========//==========//==========")
print(f'El ID del Empleado es: {employee1.getEmployeeid()}\n') 
print(f'El nombre del Empleado es  {employee1.getNameEmployee()}\n')
print(f'El salario del Empleado es {employee1.getSalary()}\n')
print(f'El rol del Empleado es {employee1.getRole()}\n')
print(f'El ranking del Empleado es {employee1.getRanking()}\n')
#print(f'El Calendario del empleado es {employee1.getScheduleEmpl}\n')
# print(f'El Calendario del empleado es {employee1.addScheduleEmpl}\n')    
  
# NOTAS :  

# Mirar bien que los nombres de los atributos concuerden con 
# sus respectivos metodos y parametros de entrada


# Pendiente por añadir el metodo addOffer()     

# Preguntar por la lista Ranking, lista scheduleempl

# hola