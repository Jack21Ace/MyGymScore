#Creación de la clase Payroll
class Payroll:

    # Declaración del constructor
    def __init__(self, __payrollId:int , __payNet:float , __percentDiscount:float ,
                __percentAid:float):
        # Datos de entrada
        self.payr=[]
        self.payrollId = __payrollId
        self.payNet = __payNet
        self.percentDiscount = __percentDiscount
        self.percentAid = __percentAid
 
# STARS METHODS
    # Getter para PayrollId
    def getPayrollId(self):
        return self.payrollId

    # Getter && Setter para payNet
    def getPayNet(self):
        return self.payNet

    def setPayNet(self, __payNet):
        self.payNet = __payNet

    # Getter && Setter para percentDiscount
    def getPercentDiscount(self):
        return self.percentDiscount

    def setPercentDiscount(self, __percentDiscount):
        self.percentDiscount = __percentDiscount

    # Getter && Setter para percentAid
    def getPercentAid(self):
        return self.percentAid

    def setPercentAid(self, __percentAid):
        self.percentAid = __percentAid
# ENDS METHODS Getter and Setter

    # metodo para obtener el total
    def totalPagar(self):
        neto = self.payNet
        netodiscount = neto*self.percentDiscount
        netoAid = neto*self.percentAid
        neto = (neto-netodiscount)+netoAid
        return neto

    def addPayroll(self, __payrollId:int, __payNet:float, __percentDiscount:float, __percentAid:float):
        payroll1= Payroll(__payrollId , __payNet , __percentDiscount , __percentAid)
        payroll1 in self.payr

# #Test Payroll
# pay1 = Payroll(10, 900000, 0.12 , 0.25)
# total = pay1.totalPagar()
# print(f"El salario neto es {pay1.getPayNet()}\n"+
#         f"El porcenteje de descuento es: {pay1.getPercentDiscount()}\n"
#         f"El porcentaje de auxilio es: {pay1.getPercentAid()}\n"
#         f"El total a pagar es: {total}")