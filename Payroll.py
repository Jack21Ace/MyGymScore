#Creación de la clase Payroll
class Payroll:

    # Declaración del constructor
    def __init__(self, __payrollId:int , __payNet:float , __percentDiscounts:float ,
                __percentAid:float):
        # Datos de entrada
        self.__payr=[]
        self.__payrollId = __payrollId
        self.__payNet = __payNet
        self.__percentDiscounts = __percentDiscounts
        self.__percentAid = __percentAid

# STARS METHODS
    # Getter para PayrollId
    def getPayrollId(self):
        return self.__payrollId

    # Getter && Setter para payNet
    def getPayNet(self):
        return self.__payNet

    def setPayNet(self, __payNet:float):
        self.__payNet = __payNet

    # Getter && Setter para percentDiscount
    def getPercentDiscounts(self):
        return self.__percentDiscounts

    def setPercentDiscounts(self, __percentDiscounts:float):
        self.__percentDiscounts = __percentDiscounts

    # Getter && Setter para percentAid
    def getPercentAid(self):
        return self.__percentAid

    def setPercentAid(self, __percentAid:float):
        self.__percentAid = __percentAid
# ENDS METHODS Getter and Setter

    # metodo para obtener el total
    def totalPagar(self):
        neto = self.__payNet
        netodiscount = neto*self.__percentDiscounts
        netoAid = neto*self.__percentAid
        neto = (neto-netodiscount)+netoAid
        return neto

    def addPayroll(self, __payrollId:int, __payNet:float, __percentDiscounts:float, __percentAid:float):
        payroll1= Payroll(__payrollId , __payNet , __percentDiscounts , __percentAid)
        payroll1 in self.payr

pay1 = Payroll(10, 900000, 0.12 , 0.25)
total = pay1.totalPagar()
print(f"El salario neto es {pay1.getPayNet()}\n"+
      f"El porcentaje de descuento es: {pay1.getPercentDiscounts()}\n"
      f"El porcentaje de auxilio es: {pay1.getPercentAid()}\n"
      f"El total a pagar es: {total}")

# #Test Payroll
# pay1 = Payroll(10, 900000, 0.12 , 0.25)
# total = pay1.totalPagar()
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f"El salario neto es {pay1.getPayNet()} con el porcenteje descuento de {pay1.getPercentDiscount()}\n"
#       f"El porcentaje de auxilio es: {pay1.getPercentAid()} y El total a pagar es: {total}")
