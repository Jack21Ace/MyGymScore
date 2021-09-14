# creación de la clase Bill
from typing import Any
from datetime import date, time
# Imports de clases
import User
import DetailBill

class Bill:
    # definición de constructor
    def __init__(self, __numberBill:int, __campusName:str, __nit:int, __nameAdmin:str, __phone:str, __address:str,
                __date:date, __time:time, __detailBill:DetailBill, __customerName: User):
        self.numberBill = __numberBill
        self.campusName = __campusName
        self.nit = __nit
        self.nameAdmin = __nameAdmin
        self.phone = __phone
        self.address = __address
        self.date = __date
        self.time = __time
        self.detailBill = __detailBill
        self.customerName = __customerName

# Inicio Metodos
    # Getter para NumberBill
    def getNumberBill(self):
        return self.numberBill

    # Getter && Setter Para campusName
    def getCampusName(self):
        return self.campusName

    def setCampusName(self, __campusName):
        self.campusName = __campusName

    # Getter && Setter Para nit
    def getNit(self):
        return self.nit

    def setNit(self, __nit):
        self.nit = __nit

    # Getter && Setter Para nameAdmin
    def getNameAdmin(self):
        return self.nameAdmin

    def setNit(self, __nameAdmin):
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

    # Getter && Setter Para time
    def getTime(self):
        return self.time

    def setTime(self, __time):
        self.time = __time

    # Getter && Setter Para detailBill
    def getDetailBill(self):
        return self.detailBill

    def setDetailBill(self, __detailBill):
        self.detailBill = __detailBill

    # Getter && Setter Para customerName
    def getCustomerName(self):
        return self.customerName

    def setCustomerName(self, __customerName):
        self.customerName = __customerName

# Instancia del objeto
bill = Bill(987456213, "Iron Fitt", 123456789, "Arturo", "3105487425", "kr 25 # 24-13", date(2021, 3, 13), time(7, 10, 5), DetailBill, User)
print("==========//==========//==========//==========//==========//==========//==========")
print(f"Su numero de factura es: {bill.getNumberBill()}\nEl nombre de la sede es {bill.getCampusName()}\n"
    f"El nit de la empresa es: {bill.getNit()}\nEl nombre de admin {bill.getNameAdmin()}\n"
    f"La fecha de la Factura es {bill.getDate()} a las {bill.getTime()}\n"
    f"Al cliente {bill.getCustomerName()}")

"""Test Bill
bill = Bill(987456213, "Iron Fitt", 123456789, "Arturo", "3105487425", "kr 25 # 24-13", date(2021, 3, 13), time(7, 10, 5), DetailBill, User)
print("==========//==========//==========//==========//==========//==========//==========")
print(f"Su numero de factura es: {bill.getNumberBill()} con el nombre de la sede {bill.getCampusName()}\n"
    f"El nit de la empresa es: {bill.getNit()} y el nombre del administrador es {bill.getNameAdmin()}\n"
    f"La fecha de la Factura es {bill.getDate()} a las {bill.getTime().value}.\n"
    f"El grupo Sangüineo del usuario es: {user.getRh().value}")"""


"""Test Employee
employee = Employee(123456, 'R2D2', '3155555555', 1200000, RoleList.ADMINISTRATOR, Ranking.CUATRO, EmployeeSchedule)
print("==========//==========//==========//==========//==========//==========//==========")
print(f"El nombre del trabajador es {employee.getNameEmployee()}, su numero de telefono es {employee.getPhoneEmpl()}\n"
    f"Su salario es {employee.getSalary()}.")"""
