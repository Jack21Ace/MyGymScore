# creación de la clase Bill
from typing import Any, List
from datetime import date
from Campus import Campus
#Imports de clases
from DetailBill import DetailBill
from Employee import Employee
from Enums import Eps, Gender, Purpose, Rh
from MedicalControl import MedicalControl
from User import User
from DetailBill import DetailBill
from Offer import Offer
from Product import Product
from UserSchedule import UserSchedule

class Bill:
    # definición de constructor
    def __init__(self, __numberBill:int, __nit:int, __nameAdmin:str, __phone:str, __address:str, __date:date, __campusInfo:Campus):

        self.__bills:List[Bill]=[]
        self.__numberBill = __numberBill
        self.__nit = __nit
        self.__nameAdmin = __nameAdmin
        self.__phone = __phone
        self.__address = __address
        self.__date = __date
        self.__campusInfo = __campusInfo
        self.__detailBill = DetailBill(101234, Offer, Product) # Composicion de DetailBill
        self.__user = User(1054995036, "Donald J.", "Herrera", Gender.MALE, "3012232219", "3148947223", "jack2119hv@gmail.com", "316497", "Manizales", 1.78, 78, True, Purpose.TONE_UP, Rh.O_NEGATIVE, Eps.SURA, date(1994,3,13), Employee, MedicalControl, UserSchedule) # Composicion User

# Inicio Metodos
    # Getter para NumberBill
    def getNumberBill(self):
        return self.__numberBill

    # Getter Para nit
    def getNit(self):
        return self.__nit

    # Getter && Setter Para nameAdmin
    def getNameAdmin(self):
        return self.__nameAdmin

    def setNameAdmin(self, __nameAdmin):
        self.__nameAdmin = __nameAdmin

    # Getter && Setter Para phone
    def getPhone(self):
        return self.__phone

    def setPhone(self, __phone):
        self.__phone = __phone

    # Getter && Setter Para address
    def getAddress(self):
        return self.__address

    def setAddress(self, __address):
        self.__address = __address

    # Getter && Setter Para date
    def getDate(self):
        return self.__date

    def setDate(self, __date):
        self.__date = __date

    # Getter && Setter Para detailBill
    def getDetailBill(self):
        return self.__detailBill

    def setDetailBill(self, __detailBill):
        self.__detailBill = __detailBill

    # getter para User
    def getUser(self):
        return self.__user

    # getter para campusInfo
    def getCampusInfo(self):
        return self.__campusInfo
    
    def addBill(self, __numberBill:int, __nit:int, __nameAdmin:str, __phone:str, __address:str, __date:date):
        bills = Bill(__numberBill, __nit, __nameAdmin, __phone, __address, __date)
        self.__bills.append(bills)
        return self.__bills

    def __str__(self):
        result = f"Gimnasio: {str(self.__campusInfo)}\nNit: {str(self.__nit)}\nNumero de la factura: {str(self.__numberBill)}\nNombre del usuario: {str(self.__user.getName())} {str(self.__user.getLastName())}\nNombre del administrador: {str(self.__nameAdmin)}\n{str(self.__phone)}\nDirección: {str(self.__address)}\nFecha de la factura: {str(self.__date)}"
        return result
