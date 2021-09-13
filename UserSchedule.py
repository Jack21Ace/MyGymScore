# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 19:27:53 2021

@author: Juan Camilo
"""
from datetime import date

#Creación de la clase userschedule
class UserSchedule:
    def __init__(self, __scheduleUserId:int, __timeZoneUser:date, __availableUser:bool):
        self.scheduleUserId = __scheduleUserId
        self.timeZoneUser = __timeZoneUser
        self.availableUser = __availableUser
    
    def getSchedule(self):
        return self.scheduleUserId  #PREGUNTAR ESTA LINEA
    
    def getTimeZone(self):
        return self.timeZoneUser
    
    def getAvailableUser(self):
        return self.availableUser
    
userschedule1 = UserSchedule(321, date(2021, 3, 14), True)

print(f'codigo: {userschedule1.getSchedule()}\nFecha: {userschedule1.getTimeZone()}\nDisponibilidad: {userschedule1.getAvailableUser()}')

