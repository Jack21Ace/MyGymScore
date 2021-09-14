from typing import Any
from Enums import Eps, Rh, Gender, Purpose, Type, ProductType, RoleList, Ranking, PayMethod, UpperBody, LowerBody, Conditioning
from datetime import date, time
from User import User#, BodyZone, Campus, DetailBill, Employee, EmployeeSchedule, Gym, Item, MedicalControl, MonthlyPay, Offer, Patology, Payroll, Product, Routine, Supplier, UserSchedule
from Routine import Routine
from MedicalControl import MedicalControl
from UserSchedule import UserSchedule
from EmployeeSchedule import EmployeeSchedule
from Bill import Bill
from MonthlyPay import MonthlyPay
from Employee import Employee

"""Test User
user = User(1054995036, 'Donald', 'Herrera', Gender.MALE, '3012232219', '3149867223', 'jack2119hv@gmail.com', 'asd.123', 'Kr 26 # 47-15', 1.78, 78, True, Purpose.DEVELOP, Rh.O_POSITIVE, Eps.ASMETSALUD, date(1994, 3, 13), MedicalControl, Routine, Ranking.CUATRO, UserSchedule, EmployeeSchedule, Any, Bill, MonthlyPay)
print("==========//==========//==========//==========//==========//==========//==========")
print(f"El nombre del usuario es {user.getName()} con numero de documento {user.getDni()}\n"
    f"Su numero telefonico es {user.getPhoneNumber()} y vive en {user.getAddress()}\n"
    f"En caso de emergencia llamar al {user.getEmergencyContact()} y la EPS es {user.getEps().value}.\n"
    f"El grupo Sangüineo del usuario es: {user.getRh().value}")"""


"""Test Employee
employee = Employee(123456, 'R2D2', '3155555555', 1200000, RoleList.ADMINISTRATOR, Ranking.CUATRO, EmployeeSchedule)
print("==========//==========//==========//==========//==========//==========//==========")
print(f"El nombre del trabajador es {employee.getNameEmployee()}, su numero de telefono es {employee.getPhoneEmpl()}\n"
    f"Su salario es {employee.getSalary()}.")"""














# Instancia del objeto User
#person1 = User(1054995036, 'Donald', 'Herrera Vargas', Gender.MALE, '3012232219', '3149847223', 'jack2119hv@gmail.com', 'asd.123', 'KR 26 # 47-15', 1.78, 78, True, Purpose, Rh.O_POSITIVE, Eps.SURA, date(2021, 3, 13), )

# person1 = User(1054995036,'Donald','Herrera Vargas', Gender.MALE, '3012232219', '3149847223', 'jack2119hv@gmail.com', 'Chupnelohpts', 'Kr 26 # 47-15', 1.78, 78, True, Purpose, Rh.O_POSITIVE, Eps.SURA, date(1994, 3, 13), MedicalControl, Routine, Ranking, UserSchedule, EmployeeSchedule, 'Historico de rutinas', Bill, MonthlyPay)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f"El nombre del usuario es {person1.getName()}\n Su apellido es {person1.getLastName()}\n"+
#     f"Su genero es {person1.getGender()}")