from Enums import UpperBody, LowerBody, Conditioning
from datetime import time
from typing import List
from BodyZone import BodyZone

class Routine:
    # Declaración del constructor
    def __init__(self, routineId:int, series:int, count:int, weight:float, timer:time):

        # Datos de entrada
        self._routineId = routineId
        self._series = series
        self._count = count
        self._weight = weight
        self._timer = timer
        self._hRutinas:list = []
        self._bodyZone = BodyZone(UpperBody.ABDOMEN, LowerBody.QUADRICEPS_FEMORIS, Conditioning.RUN) # Composicion de BodyZone

    @property
    def routineId(self):
        return self._routineId

    @property
    def series(self):
        return self._series

    @series.setter
    def series(self, series):
        self._series = series

    @series.deleter
    def series(self):
        print(f"{self._series} Eliminada!")
        del self._series


    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        self._count = count

    @count.deleter
    def count(self):
        print(f"{self._count} Eliminada!")
        del self._count


    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @weight.deleter
    def weight(self):
        print(f"{self._weight} Eliminado!")
        del self._weight


    @property
    def timer(self):
        return self._timer

    @timer.setter
    def timer(self, timer):
        self._timer = timer

    @timer.deleter
    def timer(self):
        print(f"{self._timer} Eliminado!")
        del self._timer


    @property
    def hRutinas(self):
        return self._hRutinas

    @hRutinas.setter
    def hRutinas(self, hRutinas):
        self._hRutinas = hRutinas

    @hRutinas.deleter
    def hRutinas(self):
        del self._hRutinas

    def __str__(self):
        return f"""Rutina N° {str(self._routineId)}
Compuesta por:
{str(self._series)} Series de {str(self._count)} Repeticiones
Peso: {str(self._weight)}
Hora: {str(self._timer)}
"""

