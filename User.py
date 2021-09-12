from enum import Enum
from datetime import date
from Enums import Eps, Rh, Gender

#Creación de la clase usuario
class User:
    # Declaración del constructor
    def __init__(self, __dni, __name, __lastName, __Gender, __phoneNumber,
                __emergencyContact, __emailAddress, __password, __address,
                __size, __weight, __vehicle, __purpose, __Rh, __Eps,
                __birthday, __medicalControl, __routineUser, __rankingEmpl,
                __scheduleUser, __scheduleEmpl, __routineHistory, __bill,
                __monthlyPay):
        # Datos de entrada
        """Accepts only int"""
        assert isinstance(__dni, int)
        self.dni = __dni
        self.name = __name
        self.lastName = __lastName
        self.gender = __Gender
        self.phoneNumber = __phoneNumber
        self.emergencyContact = __emergencyContact
        self.emailAddress = __emailAddress
        self.password = __password
        self.address = __address
        self.size = __size
        self.weight = __weight
        self.vehicle = __vehicle
        self.purpose = __purpose
        self.rh = __Rh
        self.eps = __Eps
        self.birthday = __birthday
        self.medicalControl = __medicalControl
        self.routineUser = __routineUser
        self.rankingEmpl = __rankingEmpl
        self.scheduleUser = __scheduleUser
        self.scheduleEmpl = __scheduleEmpl
        self.routineHistory = __routineHistory
        self.bill = __bill
        self.monthlyPay = __monthlyPay

    def getDni(self):
        return self.dni

    def getName(self):
        return self.name

    def setName(self, __name):
        self.name = __name

persona1 = User(1054995036,'Donald','Herrera Vargas', 'Masculino', '3012232219', '3149847223', 'jack2119hv@gmail.com', 'Chupnelohpts', 'Kr 26 # 47-15', 1.78, 78, True, 'Tonificar', Rh.O_POSITIVE, Eps.SURA, date(1994, 3, 13), "Sura", "Pecho", 'Ranking', 'Programación Usuario', 'Programación Usuario', 'Historico de rutinas', 'factura', 'mensualidades')
print(persona1.eps)
print(persona1.rh)


