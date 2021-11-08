# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:43:24 2021

@author: Juan Camilo
"""

from datetime import datetime

#Creación de la clase userschedule
class UserSchedule:
    def __init__(self, __scheduleUserId:int, __timeZoneUser:datetime, __availableUser:bool):
        self.__scheduleUserId = __scheduleUserId
        self.__timeZoneUser = __timeZoneUser
        self.__availableUser = __availableUser

    def getScheduleUserId(self):
        return self.__scheduleUserId  #PREGUNTAR ESTA LINEA

    def getTimeZone(self):
        return self.__timeZoneUser

    def setTimeZone(self, __timeZoneUser):
        self.__timeZoneUser = __timeZoneUser

    def getAvailableUser(self):
        return self.__availableUser

    def setAvailableUser(self, __availableUser):
        self.__availableUser = __availableUser

    def __str__(self):
        cadena = f'El Id del calendario del usuario es: {str(self.__scheduleUserId)}\nEl horario es: {str(self.__timeZoneUser)}\nLa disponibilidad es: {str(self.__availableUser)}'
        return cadena



