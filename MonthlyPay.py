# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 16:26:41 2021

@author: Juan Camilo
"""
from datetime import date
from Enums import PayMethod

#Creación de la clase MonthlyPay
class MonthlyPay:
    # Declaración del constructor
    def __init__(self, __monthlyId:int, __price:float, __dayPay:date, __deadLine:date, __payMethod:PayMethod):
        self.monthlyId = __monthlyId
        self.price = __price
        self.dayPay = __dayPay
        self.deadLine = __deadLine
        self.payMethod = __payMethod

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