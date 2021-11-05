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

    def setPrice(self, __price:int):
        self.__price = __price

    def getDayPay(self):
        return self.__dayPay

    def setDayPay(self, __daypay:date):
        self.__dayPay = __daypay
        

    def getDeadLine(self):
        return self.__deadLine

    def setDeadLine(self, __deadLine:date):
        self.__deadLine = __deadLine
        

    def getPayMethod(self):
        return self.__payMethod

    def setPayMethod(self, __paymethod:PayMethod):
        self.__payMethod = __paymethod
    
    def __str__(self):
        result = f"Total a pagar: {str(self.__price)}\nFecha pago oportuno: {str(self.__dayPay)}\nFecha Limite: {str(self.__deadLine)}\nMetodo de pago elegido: {str(self.__payMethod.value)}"
        return result
