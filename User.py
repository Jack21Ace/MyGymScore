<<<<<<< HEAD
from typing import Any, List, get_origin
from Employee import Employee
=======
from typing import Any, List
>>>>>>> ac0599c3934684bd29b085462f6c219c2f99add6
from Enums import Eps, Rh, Gender, Purpose, Ranking
from datetime import date
# Imports de las clases pendientes
"""
import RoutineHistory
"""
# imports de clases
import MedicalControl
<<<<<<< HEAD
import Routine
#import EmployeeSchedule
#import Bill
import MonthlyPay
from UserSchedule import UserSchedule
import RoutineHistory
=======
# import Routine
# import EmployeeSchedule
# import Bill
# import UserSchedule
# import RoutineHistory
>>>>>>> ac0599c3934684bd29b085462f6c219c2f99add6

#Creación de la clase usuario
class User:

    # Inicializador de la clase
    def __init__(self, __dni:int, __name:str, __lastName:str, __gender:Gender, __phoneNumber:str, __emergencyContact:str, __emailAddress:str,
     __password:str, __address:str, __size:float, __weight:float, __vehicle:bool, __purpose:Purpose, __rh:Rh, __eps:Eps, 
     __birthDate:date, __employee:Employee, __medicalControl:MedicalControl, __scheduleUser:UserSchedule):

        # Datos de entrada
        self.__dni = __dni
        self.__name = __name
        self.__lastName = __lastName
        self.__gender = __gender
        self.__phoneNumber = __phoneNumber
        self.__emergencyContact = __emergencyContact
        self.__emailAddress = __emailAddress
        self.__password = __password
        self.__address = __address
        self.__size = __size
        self.__weight = __weight
        self.__vehicle = __vehicle
        self.__purpose = __purpose
        self.__rh = __rh
        self.__eps = __eps
        self.__birthDate = __birthDate
<<<<<<< HEAD
        self.__routine = Routine() # Composición Any()
=======
        self.__bill = Any # Composición Any()
        self.__listBill:List[Any]=[] # Listas Tipadas
        self.__routine = Any # Composición Any()
        self.__routineHistory:List[Any] = [] # Listas Tipadas
        self.__monthlyPayHistory:List[Any] = [] # Listas Tipadas
>>>>>>> ac0599c3934684bd29b085462f6c219c2f99add6
        self.__employee = __employee # Agregación
        self.__scheduleUser = __scheduleUser # Agregación
        self.__medicalControl = __medicalControl # Agregación

# getter && setter STARTS
    # Getter para dni
    def getDni(self):
        return self.__dni

    # getter && setter para name
    def getName(self):
        return self.__name

    def setName(self, __name:str):
        self.__name = __name

    # getter && setter para lastName
    def getLastName(self):
        return self.__lastName

    def setLastName(self, __lastName:str):
        self.__lastName = __lastName

    # getter para Gender
    def getGender(self):
        return self.__gender

    # getter && setter para phoneNumber
    def getPhoneNumber(self):
        return self.__phoneNumber

    def setPhoneNumber(self, __phoneNumber:str):
        self.__phoneNumber = __phoneNumber

    # getter && setter para emergencyContact
    def getEmergencyContact(self):
        return self.__emergencyContact

    def setEmergencyContact(self, __emergencyContact:str):
        self.__emergencyContact = __emergencyContact

    # getter && setter para emailAddress
    def getEmailAddress(self):
        return self.__emailAddress

    def setEmailAddress(self, __emailAddress:str):
        self.__emailAddress = __emailAddress

    # getter && setter para password
    def getPassword(self):
        return self.__password

    def setPassword(self, __password:str):
        self.__password = __password

    # getter && setter para address
    def getAddress(self):
        return self.__address

    def setAddress(self, __address:str):
        self.__address = __address

    # getter && setter para size
    def getSize(self):
        return self.__size

    def setSize(self, __size:float):
        self.__size = __size

    # getter && setter para weight
    def getWeight(self):
        return self.__weight

    def setWeight(self, __weight:float):
        self.__weight = __weight

    # getter && setter para Vehicle
    def getVehicle(self):
        return self.__vehicle

    def setVehicle(self, __vehicle:bool):
        self.vehicle = __vehicle

    # getter && setter para Purpose
    def getPurpose(self):
        return self.__purpose

    def setPurpose(self, __purpose:Purpose):
        self.__purpose = __purpose

    # getter para Rh
    def getRh(self):
        return self.__rh

    # getter && setter para Eps
    def getEps(self):
        return self.__eps

    def setEps(self, __eps:Eps):
        self.__eps = __eps

    # getter para birthDate
    def getBirthDate(self):
        return self.__birthDate

    # getter && setter para Routine
    def getRoutine(self):
        # return self.Routine...parameters
        return self.__routine

    def setRoutine(self, __routine:Routine()):
        self.__routine = __routine

<<<<<<< HEAD
        # getter para Employee
=======
    # getter  para MonthlyPayHistory
    def getMonthlyPayHistory(self):
        return self.__monthlyPayHistory

    # getter para Employee
>>>>>>> ac0599c3934684bd29b085462f6c219c2f99add6
    def getEmployee(self):
        return self.__employee

    # getter && setter para MedicalControl
    def getMedicalControl(self):
        try:
            return self.__medicalControl
        except: 
            pass

    def setMedicalControl(self, __medicalControl:List[Any]):
        try:
            self.__medicalControl = __medicalControl
        except:
            pass

    # getter && setter para ScheduleUser
    def getScheduleUser(self):
        return self.__scheduleUser

    def setScheduleUser(self, __ScheduleUser:List[Any]):
        self.__scheduleUser = __ScheduleUser

    # Mejor forma para imprimir la información almacenada
    def __str__(self):
        result = f"Nuevo Usuario Registrado\nNombre: {str(self.__name)} {str(self.__lastName)}\nNumero Contacto: {str(self.__phoneNumber)}\nGenero: {str(self.__gender.value)}\nEmail:{str(self.__emailAddress)}\nFecha de Nacimiento: {str(self.__birthDate)}\nRH: {str(self.__rh.value)}\nEPS: {str(self.__eps.value)}\nContacto Emergencia: {str(self.__emergencyContact)}"
        return result

# getter && setters ENDS
############################################################################################
# Pendiente metodos de creación de rutina "addRoutine", "addMedicalControl" , "addSchedule"
# Crear funcion impirmir información.#
############################################################################################

<<<<<<< HEAD
person1 = User(1054995036, "Donald J.", "Herrea", Gender.MALE, "3012232219", "3148947223", "example@exapĺer.com","134679", "Manizales", 1.78, 78, True, Purpose.TONE_UP, Rh.O_POSITIVE, Eps.SURA, date(1994,3,13), Employee, MedicalControl, UserSchedule)
=======
person1 = User(1054995036, "Donald J.", "Herrera", Gender.MALE, "3012232219", "3148947223", "example@example.com", "123456987", "Barrio El Hueco", 1.78, 78, True, Purpose.TONE_UP, Rh.O_POSITIVE, Eps.SURA, date(1994,3,13), Any, Any, Any)
>>>>>>> ac0599c3934684bd29b085462f6c219c2f99add6
print(person1.__str__())