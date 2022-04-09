from datetime import datetime, time
from dateutil.relativedelta import relativedelta
from Enums import Eps, Rh
from Routine import Routine
class User:
    def __init__(self, nombre:str, apellido:str, dni:str, email:str, telefono:int, fechaNacimiento:datetime, rh:str, eps:str):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._email = email
        self._telefono = telefono
        self._fechaNacimiento = fechaNacimiento
        self._rh = rh
        self._eps = eps
        self._rutina = Routine(111, 4, 8, 50.0, time(6, 00)) #COMPOSICIÓN
        self._historialRutinas:Routine = []

    def __str__(self):
        return f"Nombre: {str(self._nombre)} {str(self._apellido)}\nDNI: {str(self._dni)}\nCorreo: {str(self._email)}\nEdad: {str(self._fechaNacimiento)}\nTelefono: {str(self._telefono)}\nGrupo Sanguineo: {str(self._rh)};  Eps: {str(self._eps)}\n\n=====//==Rutina Asignada==//=====\n\n{str(self._rutina)}\n\n"#=====//==Historial de Rutinas==//=====\n\n=====//=====//=====//=====//=====//====="


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

    @dni.setter
    def dni(self, dni):
        self._dni = dni

    @dni.deleter
    def dni(self):
        del self._dni


    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

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
    def fechaNacimiento(self):
        edad = relativedelta(datetime.now(), self.fechaNacimiento)
        return edad

    @fechaNacimiento.setter
    def fechaNacimiento(self, fechaNacimiento):
        self._fechaNacimiento = fechaNacimiento

    @fechaNacimiento.deleter
    def fechaNacimiento(self):
        del self._fechaNacimiento


    @property
    def rh(self):
        return self._rh

    @rh.setter
    def rh(self, rh):
        self._rh = rh

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
    def historialRutinas(self):
        return self._historialRutinas

    @historialRutinas.setter
    def historialRutinas(self, historialRutinas):
        self._historialRutinas = historialRutinas

    @historialRutinas.deleter
    def historialRutinas(self):
        del self._historialRutinas