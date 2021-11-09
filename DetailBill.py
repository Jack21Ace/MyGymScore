#Creación de la clase DetailBill
from typing import List
from Offer import Offer
from MonthlyPay import MonthlyPay
from Product import Product
from datetime import date
from Enums import PayMethod

class DetailBill:

    # Declaración del constructor
    def __init__(self, __detailCode:int, __offer:Offer, __product:Product):

        # Datos de entrada
        self.__listDetailBill = []
        self.__detailCode = __detailCode
        self.__offer = __offer
        self.__monthlyPay = MonthlyPay(123, 32.455, date(2021, 3, 14), date(2021, 3, 15), PayMethod.DEBIT_CARD)  # Composicion MonthlyPay
        self.__historyMonthlyPay:List[MonthlyPay] = []
        self.__product = __product
        self.__listProduct:List[Product] = []

    # Getter para detailCode
    def getdetailCode(self):
        return self.__detailCode

    # Getter and Setter Para Offer
    def getOffer(self):
        return self.__offer

    def setOffer(self, __offer:Offer):
        self.__offer = __offer

    # Getter and Setter Para MonthlyPay
    def getMonthlyPay(self):
        return self.__monthlyPay

    def setMonthlyPay(self, __monthlyPay:MonthlyPay):
        self.__monthlyPay = __monthlyPay

    # Getter and Setter Para MonthlyPay
    def getHistoryMonthlyPay(self):
        return self.__historyMonthlyPay

    def setHistoryMonthlyPay(self, __historyMonthlyPay:List[MonthlyPay]):
        self.__historyMonthlyPay = __historyMonthlyPay

    # Getter and Setter Para Product
    def getProduct(self):
        return self.__product

    def setProduct(self, __product:Product):
        self.__product = __product

    # Getter and Setter Para List:Product
    def getListProduct(self):
        return self.__listProduct

    def setListProduct(self, __listProduct:List[Product]):
        self.__listProduct = __listProduct

    # Metodo add para DetailBill
    def addDetailBill(self, __detailCode:int , __offer:Offer , __monthlyPay:MonthlyPay , __product:Product):
        bill = DetailBill(__detailCode, __offer, __monthlyPay, __product)
        self.__listDetailBill.append(bill)
        return self.__listDetailBill

    def __str__(self):
        cadena = f'El codigo del detalle de la factura es: {str(self.__detailCode)}\nEl nombre de la oferta es: {str(self.__offer.getName())}\nLa oferta es sobre: {str(self.__offer.getDescription())}\nEl dia de inicio de la oferta es: {str(self.__offer.getStart())} y termina el dia: {str(self.__offer.getEnd())}\nEl nombre del producto es: {str(self.__product.getProductName())}\nEl precio del producto es: {str(self.__product.getPrice())}\nLa disponibilidad del producto es: {str(self.__product.getAvailable())}\nEl pago de la mensualidad es: {str(self.__monthlyPay.getPrice())}\nEl dia de pago es: {str(self.__monthlyPay.getDayPay())}'
        return cadena

