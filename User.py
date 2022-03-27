from enum import Enum
from datetime import date
from typing import Any
from Enums import Eps, Rh, Gender, Purpose, Ranking
from datetime import date, time, datetime
# Imports de las clases pendientes
"""
#import RoutineHistory
"""
# imports de clases
import MedicalControl
import Routine
import EmployeeSchedule
import Bill
import MonthlyPay
import UserSchedule
import RoutineHistory

#Creación de la clase usuario
class User:
    # Declaración del constructor
    def __init__(self, __dni:int, __name:str, __lastName:str, __gender:Gender, __phoneNumber:str, __emergencyContact:str,
                __emailAddress:str, __password:str, __address:str, __size:float, __weight:float, __vehicle:bool,
                __purpose:Purpose, __rh:Rh, __eps:Eps, __birthday:date, __medicalControl:MedicalControl,
                __routine:Routine, __rankingEmpl:Ranking, __scheduleUser:UserSchedule, __scheduleEmpl:EmployeeSchedule,
                __routineHistory:RoutineHistory, __bill:Bill, __monthlyPay:MonthlyPay):

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
        self.birthday = __birthday
        self.medicalControl = __medicalControl
        self.routineUser = __routine
        self.rankingEmpl = __rankingEmpl
        self.scheduleUser = __scheduleUser
        self.scheduleEmpl = __scheduleEmpl
        self.routineHistory = __routineHistory
        self.bill = __bill
        self.monthlyPay = __monthlyPay

# getter && setter STARTS
    # Getter para dni
    def getDni(self):
        return self.dni

    # getter && setter para name
    def getName(self):
        return self.name

    def setName(self, __name):
        self.name = __name

    # getter && setter para lastName
    def getLastName(self):
        return self.lastName

    def setLastName(self, __lastName):
        self.lastName = __lastName

    # getter && setter para Gender
    def getGender(self):
        return self.gender

    def setGender(self, __Gender):
        self.gender = __Gender

    # getter && setter para phoneNumber
    def getPhoneNumber(self):
        return self.phoneNumber

    def setPhoneNumber(self, __phoneNumber):
        self.phoneNumber = __phoneNumber

    # getter && setter para emergencyContact
    def getEmergencyContact(self):
        return self.emergencyContact

    def setEmergencyContact(self, __emergencyContact):
        self.emergencyContact = __emergencyContact

    # getter && setter para password
    def getPassword(self):
        return self.password

    def setPassword(self, __password):
        self.password = __password

    # getter && setter para address
    def getAddress(self):
        return self.address

    def setAddress(self, __address):
        self.address = __address

    # getter && setter para size
    def getSize(self):
        return self.size

    def setSize(self, __size):
        self.size = __size

    # getter && setter para weight
    def getWeight(self):
        return self.weight

    def setWeight(self, __weight):
        self.weight = __weight

    # getter && setter para Purpose
    def getPurpose(self):
        return self.purpose

    def setPurpose(self, __Purpose):
        self.purpose = __Purpose

    # getter && setter para Rh
    def getRh(self):
        return self.rh

    def setRh(self, __Rh):
        self.rh = __Rh

    # getter && setter para Eps
    def getEps(self):
        return self.eps

    def setEps(self, __Eps):
        self.eps = __Eps

    # getter && setter para birthday
    def getBirthday(self):
        return self.birthday

    def setBirthday(self, __birthday):
        self.birthday = __birthday

    # getter && setter para MedicalControl
    def getMedicalControl(self):
        return self.medicalControl

    def setMedicalControl(self, __MedicalControl):
        self.medicalControl = __MedicalControl

    # getter && setter para Routine
    def getRoutine(self):
        return self.routine

    def setRoutine(self, __Routine):
        self.routine = __Routine

    # getter && setter para RankingEmpl
    def getRankingEmpl(self):
        return self.rankingEmpl

    def setRankingEmpl(self, __RankingEmpl):
        self.rankingEmpl = __RankingEmpl

    # getter && setter para ScheduleUser
    def getScheduleUser(self):
        return self.scheduleUser

    def setScheduleUser(self, __ScheduleUser):
        self.scheduleUser = __ScheduleUser

    # getter && setter para ScheduleEmpl
    def getScheduleEmpl(self):
        return self.scheduleEmpl

    def setScheduleEmpl(self, __ScheduleEmpl):
        self.scheduleEmpl = __ScheduleEmpl

    # getter && setter para RoutineHistory
    def getRoutineHistory(self):
        return self.routineHistory

    def setRoutineHistory(self, __RoutineHistory):
        self.routineHistory = __RoutineHistory

    # getter && setter para Bill
    def getBill(self):
        return self.bill

    def setBill(self, __Bill):
        self.bill = __Bill

    # getter && setter para MonthlyPay
    def getMonthlyPay(self):
        return self.monthlyPay

    def setMonthlyPay(self, __MonthlyPay):
        self.monthlyPay = __MonthlyPay
# getter && setters ENDS

# person1 = User(1054995036,'Donald','Herrera Vargas', Gender.MALE, '3012232219', '3149847223', 'jack2119hv@gmail.com', 'Chupnelohpts', 'Kr 26 # 47-15', 1.78, 78, True, Purpose, Rh.O_POSITIVE, Eps.SURA, date(1994, 3, 13), MedicalControl, Routine, Ranking, UserSchedule, EmployeeSchedule, RoutineHistory, Bill, MonthlyPay)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f"El nombre del usuario es {person1.getName()}\n Su apellido es {person1.getLastName()}\n"+
#     f"Su genero es {person1.getGender().value}")