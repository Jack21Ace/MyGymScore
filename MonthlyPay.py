# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:46:29 2021

@author: Juan Camilo
"""

from datetime import date
from Enums import PayMethod

#Creación de la clase MonthlyPay
class MonthlyPay:
    # Declaración del constructor
    def __init__(self, __monthlyId:int, __price:float, __dayPay:date, __deadLine:date, __payMethod:PayMethod, __dni:int, __name:str, __lastName:str, __gender:Gender, __phoneNumber:str, __emergencyContact:str,
                __emailAddress:str, __password:str, __address:str, __size:float, __weight:float, __vehicle:bool,
                __purpose:Purpose, __rh:Rh, __eps:Eps, __birthDate:date, __bill:Any, __listBill:List[Any], __routine:Any,
                __monthlyPay:Any, __monthlyPayHistory:List[Any], __employee:List[Any], __scheduleUser:List[Any], 
                __routineHistory:List[Any]):
        self.monthlyId = __monthlyId
        self.price = __price
        self.dayPay = __dayPay
        self.deadLine = __deadLine
        self.payMethod = __payMethod

    # COMPOSICIONES DE MONTHLYPAY

        #User
        __User = User()
        __User.dni = __dni
        __User.name = __name
        __User.lastName = __lastName
        __User.gender = __gender
        __User.phoneNumber = __phoneNumber
        __User.emergencyContact = __emergencyContact
        __User.emailAddress = __emailAddress
        __User.password = __password
        __User.address = __address
        __User.size = __size
        __User.weight = __weight
        __User.vehicle = __vehicle
        __User.purpose = __purpose
        __User.rh = __rh
        __User.eps = __eps
        __User.birthDate = __birthDate
        __User.bill = __bill
        __User.listBill = __listBill
        __User.routine = __routine
        __User.monthlyPay = __monthlyPay
        __User.monthlyPayHistory = __monthlyPayHistory
        __User.employee = __employee
        __User.scheduleUser = __scheduleUser
        __User.routineHistory = __routineHistory
        ##self.user = __User  DUDA

    def getMonthlyId(self):
        return self.monthlyId
    def getPrice(self):
        return self.price
    def setPrice(self, __price):
        self.price = __price
    def getDayPay(self):
        return self.dayPay
    def setDayPay(self, __daypay):
        self.daypay = __daypay
    def getDeadLine(self):
        return self.deadLine
    def setDeadLine(self, __deadline):
        self.deadline = __deadline
    def getPayMethod(self):
        return self.payMethod
    def setPayMethod(self, __paymethod):
        self.paymethod = __paymethod

# monthlypay1 = MonthlyPay(123, 32.455, date(2021, 3, 14), date(2021, 3, 15), PayMethod)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'codigo: {monthlypay1.getMonthlyId()}\n'
#         f'El total a pagar es: {monthlypay1.getPrice()}\n'
#         f'Día de pago: {monthlypay1.getDayPay()}\n'
#         f'Fecha limite {monthlypay1.getDeadLine()}')