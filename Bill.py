# creación de la clase Bill
from datetime import date, time
# Imports de clases
import DetailBill
import User

     
class Bill:
    # definición de constructor
    def __init__(self, __numberBill:int, __nit:int, __nameAdmin:str, __phone:str, __address:str,
                __date:date):
    
        self.__billr=[]
        self.__numberBill = __numberBill
        self.__nit = __nit
        self.__nameAdmin = __nameAdmin
        self.__phone = __phone
        self.__address = __address
        self.__date = __date
        self.__detailBill = DetailBill()
        self.__User = User()
 
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

    def setNameAdmin(self, __nameAdmin:str):
        self.__nameAdmin = __nameAdmin

    # Getter && Setter Para phone
    def getPhone(self):
        return self.__phone

    def setPhone(self, __phone:str):
        self.__phone = __phone

    # Getter && Setter Para address
    def getAddress(self):
        return self.__address

    def setAddress(self, __address:str):
        self.__address = __address

    # Getter && Setter Para date
    def getDate(self):
        return self.__date

    def setDate(self, __date:date):
        self.__date = __date


    # Getter && Setter Para detailBill
    def getDetailBill(self):
        return self.__detailBill

    def setDetailBill(self, __detailBill:DetailBill):
        self.__detailBill = __detailBill

#getter para User
    def getUser(self):
        return self.__User
 
      
    def addBill(self, __numberBill:int, __nit:int, __nameAdmin:str, __phone:str, __address:str,
                __date:date, __detailBill:DetailBill, __User:User):
        bill in self.__billr   
    
# # Instancia del objeto
# bill = Bill(987456213, "Iron Fitt", 123456789, "Arturo", "3105487425", "kr 25 # 24-13", date(2021, 3, 13), time(7, 10, 5), DetailBill, User)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f"Su numero de factura es: {bill.getNumberBill()}\nEl nombre de la sede es {bill.getCampusName()}\n"
#     f"El nit de la empresa es: {bill.getNit()}\nEl nombre de admin {bill.getNameAdmin()}\n"
#     f"La fecha de la Factura es {bill.getDate()} a las {bill.getTime()}\n"
#     f"Al cliente {bill.getCustomerName()}")
           
 # Test Bill
      
bill = Bill(18398, 364, "Arturo", "3146789158", "kra 25", date(2021,10, 18), __detailBill.)
print("==========//==========//==========//==========//==========//==========//==========")
print(f"Su numero de factura es {bill.getNumberBill()}\n"+
     f"El nit de la empresa es: {bill.getNit()}, y el nombre del administrador es {bill.getNameAdmin()}\n"
     f"La fecha de la Factura es {bill.getDate()}\n"
     f"Al cliente {bill.getUser()}" ) 