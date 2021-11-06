#Creación de la clase DetailBill
from typing import Any, List
import Offer
import MonthlyPay
import Product
#Product = ["Protein", "weight"]

  
 
class DetailBill:
    __listProduct:List[Any] = []
    # Declaración del constructor
    def __init__(self, __detailCode:int, __offer:Offer, __monthlyPay:MonthlyPay, __product:Product):
        # Datos de entrada
        self.__listBill = []
        self.__detailCode = __detailCode
        self.__offer = __offer
        self.__monthlyPay = __monthlyPay
        self.__product = __product
        self.__listProduct:List[Any] = []

    def getdetailCode(self):
        return self.__detailCode

    def getOffer(self):
        return self.__offer

    def setOffer(self, __offer:Offer):
        self.__offer = __offer

    def getMonthlyPay(self):
        return self.__monthlyPay

    def setMonthlyPay(self, __monthlyPay:MonthlyPay):
        self.__monthlyPay = __monthlyPay
 
    def getProduct(self):
        return self.__product

    def setProduct(self, __product:Product):
        self.__product = __product
  
    def _addDetailBill(self, __detailCode:int , __offer:Any , __monthlyPay:Any , __product:Any):
        detailBill1 = DetailBill(__detailCode, __offer, __monthlyPay, __product)
        detailBill1 in self.__listBill
 
    def AddProduct(self, __productId:int, __supplier:List[Any],__name:str, __price:float,
                __type:Any, __brand:str, __expiration:Any):
        Product1 = Product(__productId, __supplier,__price,__type,__brand,__expiration);
        self.__listProduct.append(Product1)
        
# Instancia del objeto
detailpay = DetailBill (101234, Offer, DetailBill, Any)
print("==========//==========//==========//==========//==========//==========//==========")
print(f"El código de la factura es {detailpay.getdetailCode()}\n"+
        f"Su oferta en la factura es {detailpay.getOffer()}\n"+
        f"Su pago mensual es {detailpay.getMonthlyPay()}\n"+
        f"Sus productos son {detailpay.getProduct()}")


# #Test DetailBill
# DetailBill = (User, Offer, MonthlyPay, Any)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f"El nombre del comprador es {detailpay.getdetailCode()} con su oferta en la factura es {User.getDni()}\n"
#       f"Su pago mensual es {detailpay.getMonthlyPay().value} y Sus productos son {detailpay.getProduct()}.")