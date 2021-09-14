# aquí importamos lo que podamos necesitar aparte de los modulos ya creados ejemplo, las enumeraciones
from typing import Any
from Enums import Eps, Rh, Gender, Purpose, Type, ProductType, RoleList, Ranking, PayMethod, UpperBody, LowerBody, Conditioning
#, Gym, Item, MedicalControl, MonthlyPay, Offer, Patology, Payroll, Product, Routine, Supplier, UserSchedule
# aquí importamos las clases o modulos que ya tenemos creados
from datetime import date, time
from Product import Product
from User import User
from Routine import Routine
from Offer import Offer
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
from RoutineHistory import RoutineHistory
from BodyZone import BodyZone
from Gym import Gym
from Patology import Patology


# Test Bill
# bill1 = Bill(987456213, "Iron Fitt", 123456789, "Arturo", "3105487425", "kr 25 # 24-13", date(2021, 3, 13), time(7, 10, 5), DetailBill, User)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f"Su numero de factura es: {bill1.getNumberBill()}, el nombre de la sede es {bill1.getCampusName()}\n"+
# f"El nit de la empresa es: {bill1.getNit()} y el nombre del administrador es {bill1.getNameAdmin()}\n"+
# f"La fecha de la Factura es {bill1.getDate()}, a las {bill1.getTime()}\n")


#Test DetailBill
# detailBill = DetailBill(User, Offer, MonthlyPay, Product)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f"El nombre del comprador es {user1.getName().upper()} {user1.getLastName().upper()}\n"
#         f"La oferta de la factura es {detailBill.getOffer()}\n"
#     f"Su pago mensual es {detailBill.getMonthlyPay()} y Sus productos son {detailBill.getProduct()}.")


#Test Payroll
# pay1 = Payroll(10, 900000, 0.12 , 0.25)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f"El salario neto es {pay1.getPayNet()} con el porcenteje descuento de {pay1.getPercentDiscount()}\n"
#         f"El porcentaje de auxilio es: {pay1.getPercentAid()} y El total a pagar es: {pay1.totalPagar()}")


#Test bodyzone
# bodyzone = BodyZone(UpperBody.BICEPS, LowerBody.CALF, Conditioning.RUN)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'Hoy comenzaremos con cardio, lo primero sera {bodyzone.getConditioning().value.upper()}\n'
#         f'Segudo por una rutina para tren superior cpmenzando por {bodyzone.getUpperBody().value.upper()}\n'
#         f'Para finalizar terminaremos con tren inferior comenzando por {bodyzone.getLowerBody().value.upper()}')


# # #Test emplSchedule
# emplSchedule = EmployeeSchedule(897644, time(13,30,5), True)
# print(f"La programación tiene codigo {emplSchedule.getScheduleEmplId()}\n"
#         f"La programación es para la fecha {emplSchedule.getTimeZoneEmpl()}")


# # Test Employee
# employee = Employee(123456, 'R2D2', '3155555555', 1200000, RoleList.ADMINISTRATOR, Ranking.CUATRO, EmployeeSchedule)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f"El nombre del trabajador es {employee.getNameEmployee()}, su numero de telefono es {employee.getPhoneEmpl()}\n"
#     f"Su salario es {employee.getSalary()}, el rol del empleado es de {employee.getRole().value}, y su ranking va a ser de {employee.getRanking().value}\n"
#     f"y su programación sera de luner a viernes desde las {emplSchedule.getTimeZoneEmpl()}")


# Test Gym
# gym1 = Gym(3453, 'Big Boys', 'Malabar', '3189086655', Campus)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'El nit del gym es {gym1.getNit()}\n'
#         f'El nombre del Gym es {gym1.getName()}\n'
#         f'La direccion del Gym es {gym1.getAddress()}\n'
#         f'El telefono del Gym es {gym1.getPhone()}\n'
#         f'La sede del Gym es {campus.getName()}')


# Test Item
# item1 = Item(122324, 'Colchoneta', 23, True, 'Ejercicios ABS', Type.STOOL, Supplier)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'La identificación del item es: {item1.getItemId()}\n'
#         f'El elemento es: {item1.getName()}\n'
#         f'La cantidad actual: {item1.getAmount()}\n'
#         f'Disponibilidad: {item1.getAvailable()}\n'
#         f'Descripcion: {item1.getDescription()}')

# Test medControl
# medControl = MedicalControl(1234, 'Alvaro','Desgarro Muscular','Analgesicos','Fisioterapia',date(2021, 9,28),time(13,30,5), 1.5, Patology)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'Usted presenta {medControl.getDiagnosis().upper()}, Recomendación {medControl.getSuggestions().upper()}\n'
#         f"Tambien se recomienda tomar {medControl.getTreatment().upper()} con mucha agua")


# Test monthlyPay
# monthPay = MonthlyPay(123, 32.455, date(2021, 3, 14), date(2021, 3, 15), PayMethod.CREDIT_CARD)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'codigo: {monthPay.getMonthlyId()}\n'
#         f'El total a pagar es: {monthPay.getPrice()}\n'
#         f'Día de pago: {monthPay.getDayPay()}\n'
#         f'Fecha limite {monthPay.getDeadLine()}\n'
#         f"A elegido el metodo de pago {monthPay.getPayMethod().value}")


# Test Offer
# offer1 = Offer(1232, 'Zamba', date(2021, 11, 13), date(2021, 11, 14), 'baile', True)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'Actividad {offer1.getName().upper()}\n'
#     f'Su código es {offer1.getEventCode()}\n'
#     f'La fecha de inscripción {offer1.getStart()}\n'
#     f'Plazo hasta {offer1.getEnd()}\n'
#     f'Descripción del evento {offer1.getDescription()}\n'
#     f'Disponibilidad {offer1.getAvailable()}')


# Test Patology
# patology = Patology('Artritis', 'ABC012')
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'Sufre usted de: {patology.getName()}, {patology.getCode()}')


# Test Routine
# routine1 = Routine(1, 'Tren Superior', 4, 10, 20.5, 'Donald J. Herrera', BodyZone)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'Su rutina para hoy es: {routine1.getName()} - {bodyzone.getUpperBody().value}\n'
#         f"Comiense con {routine1.getSeries()} series de {routine1.getCount()} repeticiones\n"
#         f"!RECOMENDACIONES¡ Puede hacerlo con peso muerto o ideal {routine1.getWeight()} Lb\n"
#         f"Quien asigna la rutina es {routine1.getCreatedBy().upper()}")


# Test Supplier
# supplier1 = Supplier(8525649, 'Global Sport Ltda', '(606)886-4894', 'example@example.com')
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f"Nuestro proveedor para maquinaria  es {supplier1.getName()}\n" +
# f"Su numero de contacto es {supplier1.getPhone()} \n" +
# f"Su Correo electronico es {supplier1.getEmailAddress()} \n" +
# f"Y su Nit es {supplier1.getNit()}.")


# # Test Product
# producto1 = Product(5677, Supplier, 40950, ProductType.SUPPLEMENTS, 'ActivoFUSHION', date(2021, 11, 2))
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'El ID del Producto es: {producto1.getProductId()}\n'
#         f'El nombre del Proveedor es  {supplier1.getName()}\n'
#         f'El precio del producto es {producto1.getPrice()}\n'
#         f'El tipo del producto es {producto1.getType()}\n'
#         f'La marca del producto es {producto1.getBrand()}\n'
#         f'La fecha de expiracion del producto es {producto1.getExpiration()}')


# Test Campus
# campus = Campus(96348512, 'Iron GYM', '(606) 725-8569', 'KR 48 # 64-28 piso 1', True, 10, Item, False, Supplier, Bill, Payroll)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f"Nombre de la sede {campus.getName()}\nY su numero de telefono es {campus.getPhone()}\n"+
#         f"Si la pregunta es si el GYM tiene parqueadero, la respuesta es: {campus.getParking()}\n"+
#         f"Su capacidad es {campus.getSizeParking()}.\n"
#         f"El proveedor para esta sede es {supplier1.getName()}")


# Test UserSchedule
# userschedule1 = UserSchedule(321, date(2021, 3, 14), True)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f'codigo: {userschedule1.getSchedule()}\n'
#         f'Fecha: {userschedule1.getTimeZone()}\n'
#         f'Disponibilidad: {userschedule1.getAvailableUser()}')


# Test User
# user1 = User(1054995036, 'Donald', 'Herrera', Gender.MALE, '3012232219', '3149867223', 'jack2119hv@gmail.com', 'asd.123', 'Kr 26 # 47-15', 1.78, 78, True, Purpose.DEVELOP, Rh.O_POSITIVE, Eps.ASMETSALUD, date(1994, 3, 13), MedicalControl, Routine, Ranking.CUATRO, UserSchedule, EmployeeSchedule, RoutineHistory, Bill, MonthlyPay)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f"El nombre del usuario es {user1.getName()} con numero de documento {user1.getDni()}\n"
#     f"Su numero telefonico es {user1.getPhoneNumber()} y vive en {user1.getAddress()}\n"
#     f"En caso de emergencia llamar al {user1.getEmergencyContact()} y la EPS es {user1.getEps().value}.\n"
#     f"El grupo Sangüineo del usuario es: {user1.getRh().value}")