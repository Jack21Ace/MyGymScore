# creación de la clase Bill
from typing import Any
from datetime import date
#Imports de clases
import DetailBill
import User
 
    
class Bill:
    # definición de constructor
    def __init__(self, __numberBill:int, __nit:int, __nameAdmin:str, __phone:str, __address:str,
                __date:date,  __detailBill:DetailBill, __User:User):
    
        self.billr=[]
        self.numberBill = __numberBill
        self.nit = __nit
        self.nameAdmin = __nameAdmin
        self.phone = __phone
        self.address = __address
        self.date = __date
        self.detailBill = __detailBill
        self.User = __User

# Inicio Metodos
    # Getter para NumberBill
    def getNumberBill(self):
        return self.numberBill

    # Getter Para nit
    def getNit(self):
        return self.nit

    # Getter && Setter Para nameAdmin
    def getNameAdmin(self):
        return self.nameAdmin

    def setNameAdmin(self, __nameAdmin):
        self.nameAdmin = __nameAdmin

    # Getter && Setter Para phone
    def getPhone(self):
        return self.phone

    def setPhone(self, __phone):
        self.phone = __phone

    # Getter && Setter Para address
    def getAddress(self):
        return self.address

    def setAddress(self, __address):
        self.address = __address

    # Getter && Setter Para date
    def getDate(self):
        return self.date

    def setDate(self, __date):
        self.date = __date


    # Getter && Setter Para detailBill
    def getDetailBill(self):
        return self.detailBill

    def setDetailBill(self, __detailBill):
        self.detailBill = __detailBill

#getter para User
    def getUser(self):
        return self.User
 
       
    def addBill(self, __numberBill:int, __nit:int, __nameAdmin:str, __phone:str, __address:str,
                __date:date, __detailBill:DetailBill, __User:User):
        bill in self.billr   
   
# # Instancia del objeto
# bill = Bill(987456213, "Iron Fitt", 123456789, "Arturo", "3105487425", "kr 25 # 24-13", date(2021, 3, 13), time(7, 10, 5), DetailBill, User)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f"Su numero de factura es: {bill.getNumberBill()}\nEl nombre de la sede es {bill.getCampusName()}\n"
#     f"El nit de la empresa es: {bill.getNit()}\nEl nombre de admin {bill.getNameAdmin()}\n"
#     f"La fecha de la Factura es {bill.getDate()} a las {bill.getTime()}\n"
#     f"Al cliente {bill.getCustomerName()}")
          
 # Test Bill
 
bill = Bill(987456213, 123456789, "Arturo", "3105487425", "kr 25 # 24-13", date(2021, 3, 13), Any, Any)
print("==========//==========//==========//==========//==========//==========//==========")
print(f"Su numero de factura es {bill.getNumberBill()}\n"+
     f"El nit de la empresa es: {bill.getNit()}, y el nombre del administrador es {bill.getNameAdmin()}\n"
     f"La fecha de la Factura es {bill.getDate()}\n"
     f"Al cliente {bill.getUser()}")
     #.getName()}" ) 