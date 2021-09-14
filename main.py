from typing import Any
from Enums import Eps, Rh, Gender, Purpose, Type, ProductType, RoleList, Ranking, PayMethod, UpperBody, LowerBody, Conditioning
from datetime import date, time
from User import User #, BodyZone, Campus, DetailBill, Employee, EmployeeSchedule, Gym, Item, MedicalControl, MonthlyPay, Offer, Patology, Payroll, Product, Routine, Supplier, UserSchedule
from Routine import Routine
from MedicalControl import MedicalControl
from UserSchedule import UserSchedule
from EmployeeSchedule import EmployeeSchedule
from Bill import Bill
from MonthlyPay import MonthlyPay
from Employee import Employee
from Campus import Campus
from Item import Item
from Supplier import Supplier
from Payroll import Payroll
from DetailBill import DetailBill

"""Test User
user = User(1054995036, 'Donald', 'Herrera', Gender.MALE, '3012232219', '3149867223', 'jack2119hv@gmail.com', 'asd.123', 'Kr 26 # 47-15', 1.78, 78, True, Purpose.DEVELOP, Rh.O_POSITIVE, Eps.ASMETSALUD, date(1994, 3, 13), MedicalControl, Routine, Ranking.CUATRO, UserSchedule, EmployeeSchedule, Any, Bill, MonthlyPay)
print("==========//==========//==========//==========//==========//==========//==========")
print(f"El nombre del usuario es {user.getName()} con numero de documento {user.getDni()}\n"
    f"Su numero telefonico es {user.getPhoneNumber()} y vive en {user.getAddress()}\n"
    f"En caso de emergencia llamar al {user.getEmergencyContact()} y la EPS es {user.getEps().value}.\n"
    f"El grupo Sangüineo del usuario es: {user.getRh().value}")"""


"""# Test Employee
employee = Employee(123456, 'R2D2', '3155555555', 1200000, RoleList.ADMINISTRATOR, Ranking.CUATRO, EmployeeSchedule)
print("==========//==========//==========//==========//==========//==========//==========")
print(f"El nombre del trabajador es {employee.getNameEmployee()}, su numero de telefono es {employee.getPhoneEmpl()}\n"
    f"Su salario es {employee.getSalary()}, el rol del empleado es de {employee.getRole().value}, y su ranking va a ser de {employee.getRanking().value}\n")"""

"""# Test Campus 
campus = Campus(96348512, 'Iron GYM', '(606) 725-8569', 'KR 48 # 64-28 piso 1', True, 10, Item, False, Supplier, Bill, Payroll)
print("==========//==========//==========//==========//==========//==========//==========")
print(f"Nombre de la sede {campus.getName()}\nY su numero de telefono es {campus.getPhone()}\n"+
f"Si la pregunta es si el GYM tiene parqueadero, la respuesta es: {campus.getParking()}\n"+
f"Su capacidad es {campus.getSizeParking()}.")"""
    
"""# Test Bill
bill1 = Bill(987456213, "Iron Fitt", 123456789, "Arturo", "3105487425", "kr 25 # 24-13", date(2021, 3, 13), time(7, 10, 5), DetailBill, User)
print("==========//==========//==========//==========//==========//==========//==========")
print(f"Su numero de factura es: {bill1.getNumberBill()}, el nombre de la sede es {campus.getName()}\n"+
f"El nit de la empresa es: {bill1.getNit()} y el nombre del administrador es {bill1.getNameAdmin()}\n"+
f"La fecha de la Factura es {bill1.getDate().value}, a las {bill1.getTime().value}\n")"""


"""#Test DetailBill
DetailBill = (User, Offer, MonthlyPay, Any)
print("==========//==========//==========//==========//==========//==========//==========")
print(f"El nombre del comprador es {detailpay.getNameClient()} con su oferta en la factura es {User.getDni()}\n"
    f"Su numero telefonico es {User.getPhoneNumber()} y vive en {User.getAddress()}\n"
    f"Su pago mensual es {detailpay.getMonthlyPay().value} y Sus productos son {detailpay.getProduct()}.")"""


#Test Payroll
# pay1 = Payroll(10, 900000, 0.12 , 0.25)
# total = pay1.totalPagar()
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f"El salario neto es {pay1.getPayNet()} con el porcenteje descuento de {pay1.getPercentDiscount()}\n"
#       f"El porcentaje de auxilio es: {pay1.getPercentAid().value} y El total a pagar es: {total}")




 








# Instancia del objeto User
#person1 = User(1054995036, 'Donald', 'Herrera Vargas', Gender.MALE, '3012232219', '3149847223', 'jack2119hv@gmail.com', 'asd.123', 'KR 26 # 47-15', 1.78, 78, True, Purpose, Rh.O_POSITIVE, Eps.SURA, date(2021, 3, 13), )

# person1 = User(1054995036,'Donald','Herrera Vargas', Gender.MALE, '3012232219', '3149847223', 'jack2119hv@gmail.com', 'Chupnelohpts', 'Kr 26 # 47-15', 1.78, 78, True, Purpose, Rh.O_POSITIVE, Eps.SURA, date(1994, 3, 13), MedicalControl, Routine, Ranking, UserSchedule, EmployeeSchedule, 'Historico de rutinas', Bill, MonthlyPay)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f"El nombre del usuario es {person1.getName()}\n Su apellido es {person1.getLastName()}\n"+
#     f"Su genero es {person1.getGender()}")