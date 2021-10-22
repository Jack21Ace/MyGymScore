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
        self.__scheduleUserId = __scheduleUserId
        self.__timeZoneUser = __timeZoneUser
        self.__availableUser = __availableUser
        self.__user = __user

    def getSchedule(self):
        return self.__scheduleUserId  #PREGUNTAR ESTA LINEA

    def getTimeZone(self):
        return self.__timeZoneUser

    def setTimeZone(self, __timeZoneUser):
        self.__timeZoneUser = __timeZoneUser

    def getAvailableUser(self):
        return self.__availableUser

    def setAvailableUser(self, __availableUser):
        self.__availableUser = __availableUser