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
    def __init__(self, __monthlyId:int, __price:float, __dayPay:date, __deadLine:date, __payMethod:PayMethod):
        self.__monthlyId = __monthlyId
        self.__price = __price
        self.__dayPay = __dayPay
        self.__deadLine = __deadLine
        self.__payMethod = __payMethod

    def getMonthlyId(self):
        return self.__monthlyId
    def getPrice(self):
        return self.__price
    def setPrice(self, __price):
        self.__price = __price
    def getDayPay(self):
        return self.__dayPay
    def setDayPay(self, __daypay):
        self.__daypay = __daypay
    def getDeadLine(self):
        return self.__deadLine
    def setDeadLine(self, __deadline):
        self.__deadline = __deadline
    def getPayMethod(self):
        return self.__payMethod
    def setPayMethod(self, __paymethod):
        self.__paymethod = __paymethod

# monthlypay1 = MonthlyPay(123, 32.455, date(2021, 3, 14), date(2021, 3, 15), PayMethod)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'codigo: {monthlypay1.getMonthlyId()}\n'
#         f'El total a pagar es: {monthlypay1.getPrice()}\n'
#         f'Día de pago: {monthlypay1.getDayPay()}\n'
#         f'Fecha limite {monthlypay1.getDeadLine()}')