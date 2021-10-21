from typing import Any, List
from Enums import Eps, Rh, Gender, Purpose, Ranking
from datetime import date
# Imports de las clases pendientes
"""
import RoutineHistory
"""
# imports de clases
# import MedicalControl
# import Routine
# import EmployeeSchedule
# import Bill
# import MonthlyPay
# import UserSchedule
# import RoutineHistory

#Creación de la clase usuario
class User(object):
    # Declaración del constructor
    def __init__(self, __dni:int, __name:str, __lastName:str, __gender:Gender, __phoneNumber:str, __emergencyContact:str,
                __emailAddress:str, __password:str, __address:str, __size:float, __weight:float, __vehicle:bool,
                __purpose:Purpose, __rh:Rh, __eps:Eps, __birthDate:date, __bill:Any, __listBill:List[Any], __routine:Any,
                __monthlyPay:Any, __monthlyPayHistory:List[Any], __employee:List[Any], __scheduleUser:List[Any], 
                __routineHistory:List[Any]):

        # Datos de entrada
        self.dni = __dni
        self.name = __name
        self.lastName = __lastName
        self.gender = __gender
        self.phoneNumber = __phoneNumber
        self.emergencyContact = __emergencyContact
        self.emailAddress = __emailAddress
        self.password = __password
        self.address = __address
        self.size = __size
        self.weight = __weight
        self.vehicle = __vehicle
        self.purpose = __purpose
        self.rh = __rh
        self.eps = __eps
        self.birthDate = __birthDate
        self.bill = __bill
        self.listBill = __listBill
        self.routine = __routine
        self.routineHistory = __routineHistory
        self.monthlyPay = __monthlyPay
        self.monthlyPayHistory = __monthlyPayHistory
        self.employee = __employee
        self.scheduleUser = __scheduleUser
        self.medicalControl = Any
        # Hasta no ser creada la clase de Medical control, no puedo hacer la agregación.
        #self.medicalControl = MedicalControl

# getter && setter STARTS
    # Getter para dni
    def getDni(self):
        return self.dni

    # getter && setter para name
    def getName(self):
        return self.name

    def setName(self, __name:str):
        self.name = __name

    # getter && setter para lastName
    def getLastName(self):
        return self.lastName

    def setLastName(self, __lastName:str):
        self.lastName = __lastName

    # getter para Gender
    def getGender(self):
        return self.gender

    # getter && setter para phoneNumber
    def getPhoneNumber(self):
        return self.phoneNumber

    def setPhoneNumber(self, __phoneNumber:str):
        self.phoneNumber = __phoneNumber

    # getter && setter para emergencyContact
    def getEmergencyContact(self):
        return self.emergencyContact

    def setEmergencyContact(self, __emergencyContact:str):
        self.emergencyContact = __emergencyContact

    # getter && setter para emailAddress
    def getEmailAddress(self):
        return self.emailAddress

    def setEmailAddress(self, __emailAddress:str):
        self.emailAddress = __emailAddress

    # getter && setter para password
    def getPassword(self):
        return self.password

    def setPassword(self, __password:str):
        self.password = __password

    # getter && setter para address
    def getAddress(self):
        return self.address

    def setAddress(self, __address:str):
        self.address = __address

    # getter && setter para size
    def getSize(self):
        return self.size

    def setSize(self, __size:float):
        self.size = __size

    # getter && setter para weight
    def getWeight(self):
        return self.weight

    def setWeight(self, __weight:float):
        self.weight = __weight

    # getter && setter para Purpose
    def getPurpose(self):
        return self.purpose

    def setPurpose(self, __Purpose:Purpose):
        self.purpose = __Purpose

    # getter para Rh
    def getRh(self):
        return self.rh

    # getter && setter para Eps
    def getEps(self):
        return self.eps

    def setEps(self, __Eps:Eps):
        self.eps = __Eps

    # getter para birthDate
    def getBirthDate(self):
        return self.birthDate

    #getter para Bill
    def getBill(self):
        return self.bill

    #getter para ListBill
    def getListBill(self):
        return self.listBill

    # getter && setter para Routine
    def getRoutine(self):
        return self.routine

    def setRoutine(self, __routine:Any):
        self.routine = __routine

    # getter && setter para RoutineHistory
    def getRoutineHistory(self):
        return self.routineHistory

    # getter && setter para MonthlyPay
    def getMonthlyPay(self):
        return self.monthlyPay

    # getter  para MonthlyPayHistory
    def getMonthlyPayHistory(self):
        return self.monthlyPayHistory

    # getter para Employee
    def getEmployee(self):
        return self.employee

    # getter && setter para MedicalControl
    def getMedicalControl(self):
        try:
            return self.medicalControl
        except:
            pass

    def setMedicalControl(self, __medicalControl:List[Any]):
        try:
            self.medicalControl = __medicalControl
        except:
            pass

    # getter && setter para ScheduleUser
    def getScheduleUser(self):
        return self.scheduleUser

    def setScheduleUser(self, __ScheduleUser:List[Any]):
        self.scheduleUser = __ScheduleUser

# getter && setters ENDS
############################################################################################
# Pendiente metodos de creación de rutina "addRoutine", "addMedicalControl" , "addSchedule"#
############################################################################################

person1 = User(1054995036, "Donald J.", "Herrera", Gender.MALE, "3012232219", "3148947223", "example.example.com", "123456789D", "Kr 26 # 47-15", 1.78, 78, True, Purpose.TONE_UP, Rh.O_POSITIVE, Eps.SURA, date(1994, 3, 13), Any, List[Any], Any, Any, List[Any], List[Any], List[Any], List[Any])
print("==========//==========//==========//==========//==========//==========//==========")
print(f"Nuevo Usuario Registrado \n",
        f"Nombre: {person1.getName().upper()} {person1.getLastName().upper()} \n",
        f"Genero: {person1.getGender().value.upper()}\n",
        f"Numero de Contacto: {person1.getPhoneNumber()}\n",
        f"Email: {person1.getEmailAddress().upper()}\n",
        f"Fecha de Nacimiento: {person1.getBirthDate()}\n",
        f"RH: {person1.getRh().value.upper()}\n",
        f"EPS: {person1.getEps().value.upper()}\n",
        f"Contacto Emergencia: {person1.getEmergencyContact()}")