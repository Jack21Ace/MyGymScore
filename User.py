from datetime import time
from Routine import Routine


class User:


    def __init__(self, nombre: str, apellido: str, dni: str, email: str, telefono: str, edad: int, rh: str, eps: str, medicalControl:list):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._email = email
        self._telefono = telefono
        self._edad = edad
        self._rh = rh
        self._eps = eps
        self._rutina = Routine(111, 4, 8, 50.0, time(6, 00), "Acondicionamiento")  # COMPOSICIÓN
        self._medicalControl:list = medicalControl
        self.sizeMedicalControl = 4


# Getter and Setter
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @nombre.deleter
    def nombre(self):
        del self._nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @apellido.deleter
    def apellido(self):
        del self._apellido

    @property
    def dni(self):
        return self._dni

    @dni.deleter
    def dni(self):
        del self._dni

    @property
    def email(self):
        return self._email

    @email.deleter
    def email(self):
        del self._email

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    @telefono.deleter
    def telefono(self):
        del self._telefono

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @edad.deleter
    def edad(self):
        del self._edad

    @property
    def rh(self):
        return self._rh

    @rh.deleter
    def rh(self):
        del self._rh

    @property
    def eps(self):
        return self._eps

    @eps.setter
    def eps(self, eps):
        self._eps = eps

    @eps.deleter
    def eps(self):
        del self._eps

    @property
    def rutina(self):
        return self._rutina

    @rutina.setter
    def rutina(self, rutina):
        self._rutina = rutina

    @rutina.deleter
    def rutina(self):
        del self._rutina

    @property
    def medicalControl(self):
        self._medicalControl

    @medicalControl.setter
    def medicalControl(self, medicalControl):
        self._medicalControl = medicalControl

    @medicalControl.deleter
    def medicalControl(self):
        del self._medicalControl

    def __str__(self):
        return f"Nombre: {str(self.nombre)} {str(self.apellido)}\nDNI: {str(self.dni)}\nCorreo: {str(self.email)}\nEdad: {self.edad}\nTelefono: {str(self.telefono)}\nGrupo Sanguineo: {str(self.rh)}; Eps: {str(self.eps)}\n\n=====//==Rutina Asignada==//=====\n\n{str(self.rutina)}\n\n=====//==Historial Medico==//=====\n\n{str(self.medicalControl)}\n\n=====//=====//=====//=====//=====//====="

    # INICIO quick sort para usuarios
    def optUsuarios(data):
        def partition(data, start, end, compare_func):
            pivot = data[start]
            low = start + 1
            high = end
            while True:

                while low <= high and compare_func(data[high], pivot):
                    high = high - 1
                while low <= high and not compare_func(data[low], pivot):
                    low = low + 1
                if low <= high:
                    data[low], data[high] = data[high], data[low]
                else:
                    break

            data[start], data[high], = data[high], data[start]
            return high
        def quickSort(data, start, end, compare_func):
            if start >= end:
                return
            p = partition(data, start, end, compare_func)
            quickSort(data, start, p-1, compare_func)
            quickSort(data, p+1, end, compare_func)

        quickSort(data, 0, len(data) -1, lambda x, y : x.edad < y.edad)
        for usr in data:
            print(usr)
        return data
    # FINAL quick sort para usuarios 

