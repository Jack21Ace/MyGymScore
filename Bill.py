# creación de la clase Bill
from typing import Any
from datetime import date
#Imports de clases
from DetailBill import DetailBill
from User import User
from DetailBill import DetailBill
from Offer import Offer
from Product import Product 
    
class Bill:
    # definición de constructor
    def __init__(self, __numberBill:int, __nit:int, __nameAdmin:str, __phone:str, __address:str, __date:date):
    
        self.__bills=[]
        self.__numberBill = __numberBill
        self.__nit = __nit
        self.__nameAdmin = __nameAdmin
        self.__phone = __phone
        self.__address = __address
        self.__date = __date
        self.__detailBill = DetailBill(101234, Offer, Product) # Composicion de DetailBill
        self.__user = User() # Composicion User 

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
 
       
    def addBill(self, __numberBill:int, __nit:int, __nameAdmin:str, __phone:str, __address:str, __date:date):
        __bills = Bill(__numberBill, __nit, __nameAdmin, __phone, __address, __date)
        self.__bills.append(__bills)
        return self.__bills



    def __str__(self) -> str:
        result = f"Codigo de la factura {str(self.__numberBill)}"
        return result
 
# bill = Bill(987456213, 123456789, "Arturo", "3105487425", "kr 25 # 24-13", date(2021, 3, 13), Any, Any)
# print("===================")
# print(bill.__str__())
