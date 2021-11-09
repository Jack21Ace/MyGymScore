from typing import Any, List
from Employee import Employee
from Enums import Eps, Rh, Gender, Purpose, Ranking
from datetime import datetime, date, time
from MedicalControl import MedicalControl
from Routine import Routine
from Patology import Patology
from UserSchedule import UserSchedule

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
        self.__routine = Routine(123, 4, 13, 20.5, Employee, time(8, 30)) # Composición ()
        self.__routineHistory:List[self.__routine] = [] # Listas Tipadas
        self.__employee = __employee # Agregación
        self.__scheduleUser = __scheduleUser # Agregación
        self.__historyScheduleUser = []
        self.__medicalControl = __medicalControl # Agregación 
        self.__historymedicalControl = []

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

    # Metodo ADD para Routine
    def addRoutine(self, __routineId:int, __series:int, __count:int, __weight:float, __createdBy:Employee, __timer:datetime):
        self.__routine = Routine(__routineId, __series, __count, __weight, __createdBy, __timer)
        self.__routineHistory.append(self.__routine)
        return self.__routineHistory

    def getRoutine(self):
        return self.__routine

    def setRoutine(self, __routine:Routine):
        self.__routine = __routine

    # getter para Employee
    def getEmployee(self):
        return self.__employee
    
    # Metodo ADD para Medicalcontrol
    def addmedicalControl(self, __medicEmploName:str, __diagnosis:str, __treatment:str, __suggestions:str, __medicalDate:date,
    __evolutionaryLevel:float, __patologies:List[Patology]):
        self.__medicalControl = MedicalControl(__medicEmploName, __diagnosis, __treatment, __suggestions, __medicalDate, __evolutionaryLevel, __patologies)
        self.__historymedicalControl.append(self.__medicalControl)
        return self.__historymedicalControl

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

# Metodo ADD Para UserSchedule 
    def addUserSchedule(self, __scheduleUserId:int, __timeZoneUser:datetime, __availableUser:bool):
        self.__ScheduleUser = UserSchedule(__scheduleUserId, __timeZoneUser, __availableUser)
        self.__historyScheduleUser.append(self.__ScheduleUser)
        return self.__historyScheduleUser

    # getter && setter para ScheduleUser
    def getScheduleUser(self):
        return self.__scheduleUser

    def setScheduleUser(self, __ScheduleUser:List[Any]):
        self.__scheduleUser = __ScheduleUser

# getter && setters ENDS

    # Mejor forma para imprimir la información almacenada
    def __str__(self):
        result = f"Nuevo Usuario Registrado\nNombre: {str(self.__name)} {str(self.__lastName)}\nNumero Contacto: {str(self.__phoneNumber)}\nGenero: {str(self.__gender.value)}\nEmail:{str(self.__emailAddress)}\nFecha de Nacimiento: {str(self.__birthDate)}\nRH: {str(self.__rh.value)}\nEPS: {str(self.__eps.value)}\nContacto Emergencia: {str(self.__emergencyContact)}\n\n===== AGREGACIÓN CON CONTROL MEDICO EN USUARIO =====\n{str(self.__medicalControl)}\n\n===== AGREGACIÓN CON PROGRAMACIÓN DE RUTINA EN USUARIO =====\n{str(self.__scheduleUser)}"
        return result

