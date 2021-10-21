# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:43:24 2021

@author: Juan Camilo
"""

from datetime import date
from User import User
#Creación de la clase userschedule
class UserSchedule:
    def __init__(self, __scheduleUserId:int, __timeZoneUser:date, __availableUser:bool, __user:User):
        self.scheduleUserId = __scheduleUserId
        self.timeZoneUser = __timeZoneUser
        self.availableUser = __availableUser
        self.user = __user

    def getSchedule(self):
        return self.scheduleUserId  #PREGUNTAR ESTA LINEA

    def getTimeZone(self):
        return self.timeZoneUser

    def setTimeZone(self, __timeZoneUser):
        self.timeZoneUser = __timeZoneUser

    def getAvailableUser(self):
        return self.availableUser

    def setAvailableUser(self, __availableUser):
        self.availableUser = __availableUser