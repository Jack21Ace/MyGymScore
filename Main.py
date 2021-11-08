from datetime import date, time, datetime
from Enums import Type, PayMethod, Ranking, Role, UpperBody, LowerBody, Conditioning
from Payroll import Payroll
from EmployeeSchedule import EmployeeSchedule
from Supplier import Supplier
from Item import Item
from MonthlyPay import MonthlyPay
from Patology import Patology
from MedicalControl import MedicalControl
from Offer import Offer
from Employee import Employee
from Product import Product
from DetailBill import DetailBill
from BodyZone import BodyZone
from Routine import Routine
from UserSchedule import UserSchedule

# PAYROLL
print("==========//==========//PAYROLL//==========//==========")
pay1 = Payroll(10, 900000, 0.12 , 0.25)
print("\n" + pay1.__str__() + "\n")
# SCHEDULEEMPLOYEE
print("==========//==========//SCHEDULEEMPLOYEE//==========//==========")
scheemployee1 = EmployeeSchedule(456, time(8,00), True, 2, 0, 8)
print("\n" + scheemployee1.__str__() + "\n")
# SUPPLIER
print("==========//==========//SUPPLIER//==========//==========")
supplier1 = Supplier(8525649, 'Global Sport Ltda', '(606)886-4894', 'example@example.com')
print("\n" + supplier1.__str__() + "\n")
# ITEM  
print("==========//==========//ITEM//==========//==========")
item1 = Item(122324, 'Colchoneta', 23, True, 'Ejercicios ABS', Type.PAD, supplier1.getName()) 
print("\n" + item1.__str__() + "\n") 
# MONTHLYPAY 
print("==========//==========//MONTHLYPAY//==========//==========")
monthlypay1 = MonthlyPay(123, 32.455, date(2021, 3, 14), date(2021, 3, 15), PayMethod.DEBIT_CARD)
print("\n" + monthlypay1.__str__()+ "\n")  
# PATOLOGY 
print("==========//==========//PATOLOGY//==========//==========")
patology1 = Patology('Embolia Cerebral', 'ABC012')
print("\n" + patology1.__str__() + "\n") 
# MEDICALCONTROL
print("==========//==========//MEDICALCONTROL//==========//==========")
medicalControl1 = MedicalControl("DR. Rojas", "Paciente que presenta una embolia ya que es bien pendejo", "Anticoagulantes", "Mejor no arriesgarnos", date(2021, 11, 4), 0.0, patology1.getCode())
print("\n" + medicalControl1.__str__() + "\n") 
# OFFER
print("==========//==========//Offer//==========//==========")
offer1 = Offer(1232, 'Zamba', date(2021, 11, 13), date(2021, 11, 14), 'baile', True)
print("\n" + offer1.__str__() + "\n")  
# EMPLOYEE
print("==========//==========//EMPLOYEE//==========//==========")
employee1 = Employee(2375, 'Oscar Andres', '317 8613343', 250000, Role.ADMINISTRATOR, Ranking.DOS)
print("\n" + employee1.__str__() + "\n" )
# PRODUCT
print("==========//==========//PRODUCT//==========//==========")
product1 = Product(134679, "Termo", 5.500, "NIKE", None, True, supplier1.getName())
print("\n" + product1.__str__() + "\n" ) 

# DETAILBILL
print("==========//==========//DETAILBILL//==========//==========")
detailpay = DetailBill(101234, offer1, product1)
print("\n" + detailpay.__str__() + "\n" ) 
# BODYZONE
print("==========//==========//BODYZONE//==========//==========")
bodyzone1 = BodyZone(UpperBody.ABDOMEN, LowerBody.QUADRICEPS_FEMORIS, Conditioning.RUN)
print("\n" + bodyzone1.__str__() + "\n" ) 
# ROUTINE
print("==========//==========//ROUTINE//==========//==========")
routine1 = Routine(123, 4, 13, 20.5, employee1.getNameEmployee(), time(8, 30))
print("\n" + routine1.__str__() + "\n" )  
# USERSCHEDULE
print("==========//==========//USERSCHEDULE//==========//==========")
userSchedule = UserSchedule(123, datetime.strptime("08/11/21 14:30", "%d/%m/%y %H:%M").ctime(), True)
print(userSchedule.__str__())
# GYM
# CAMPUS
# BILL
# USER