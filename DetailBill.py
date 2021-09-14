# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 16:42:07 2021

@author: Arturo
"""
from typing import Any
import User
import Offer
import MonthlyPay
import Product
#Product = ["Protein", "weight"]



class DetailBill:
    # Declaración del constructor
    def __init__(self, __nameClient:User, __offer:Offer, __monthlyPay:MonthlyPay, __product:Product):
        # Datos de entrada
        self.listBill = []
        self.nameClient = __nameClient
        self.offer = __offer
        self.monthlyPay = __monthlyPay
        self.product = __product

    def getNameClient(self):
        return self.nameClient

    def setNameClient(self, __nameClient):
        self.nameClient = __nameClient

    def getOffer(self):
        return self.offer

    def setOffer(self, __offer):
        self.offer = __offer

    def getMonthlyPay(self):
        return self.monthlyPay

    def setMonthlyPay(self, __monthlyPay):
        self.monthlyPay = __monthlyPay

    def getProduct(self):
        return self.product

    def setProduct(self, __product):
        self.product = __product

    def _addDetailBill(self, __nameClient:User , __offer:Offer , __monthlyPay:MonthlyPay , __product:Any):
        detailBill1 = DetailBill(__nameClient, __offer, __monthlyPay, __product)
        detailBill1 in self.listBill

# Instancia del objeto
detailpay = DetailBill (User, Offer, MonthlyPay, Any)
print("==========//==========//==========//==========//==========//==========//==========")
print(f"El nombre del comprador es {detailpay.getNameClient()}\n"+
        f"Su oferta en la factura es {detailpay.getOffer()}\n"+
        f"Su pago mensual es {detailpay.getMonthlyPay()}\n"+
        f"Sus productos son {detailpay.getProduct().value}")


# #Test DetailBill
# DetailBill = (User, Offer, MonthlyPay, Any)
# print("==========//==========//==========//==========//==========//==========//==========")
# print(f"El nombre del comprador es {detailpay.getNameClient()} con su oferta en la factura es {User.getDni()}\n"
#     f"Su numero telefonico es {User.getPhoneNumber()} y vive en {User.getAddress()}\n"
#     f"Su pago mensual es {detailpay.getMonthlyPay().value} y Sus productos son {detailpay.getProduct()}.")