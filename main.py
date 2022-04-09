    # def read(data):
    #     result = list(map(lambda a,b,c,d,e,f,g,h:(a,b,c,d,e,f,g,h), data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
    #     print(result)

from asyncore import read
from typing import Any, Type
from User import User
from Routine import Routine
from Enums import Eps, Rh
from datetime import time, datetime
from itemCrud import Item
from productCrud import Product
from SupplierCrud import Proveedor
from GymCrud import Gym
from CampusCrud import Campus

if __name__ == '__main__':

    #Este metodo NO SE USA
    def optUser():
        # def create():
    #     nombre = str(input("Ingrese nombre: "))
    #     apellido = str(input("Ingrese apellido: "))
    #     dni = str(input("Ingrese dni: "))
    #     email = str(input("Ingrese email: "))
    #     fechNacimiento = str(input("Ingrese fechNacimiento: "))
    #     telefono = str(input("Ingrese telefono: "))
    #     rh = str(input("Ingrese rh: "))
    #     eps = str(input("Ingrese eps: "))
    #     nuevoUsuario = User(nombre, apellido, dni, email, fechNacimiento, telefono, rh, eps)
    #     data.append(nuevoUsuario)
    # def read():
    #     print("-------Lista de Usuarios-------\n")
    #     for i in range(0, len(data)):
    #         print(f"{i+1}-)\n{data[i]}")
    # def update():
    #     read()
    #     i = int(input("Ingrese el numero de contacto que desea Modificar: "))
    #     opt = int(input("1-) Modificar Dtos Usuario\n2-) Modificar Dtos Rutina "))
    #     if opt == 1:
    #         nombre = str(input("Ingrese nuevo Nombre: "))
    #         data[i -1].nombre = nombre
    #         apellido = str(input("Ingrese nuevo Apellido: "))
    #         data[i -1].apellido = apellido
    #         dni = str(input("Ingrese nuevo DNI: "))
    #         data[i -1].dni = dni
    #         email = str(input("Ingrese nuevo Correo: "))
    #         data[i -1].email = email
    #         fechaNaci = str(input("Ingrese nueva Fecha Nacimiento: "))
    #         data[i -1].fechaNacimiento = fechaNaci
    #         telefono = str(input("Ingrese nuevo Telefono: "))
    #         data[i -1].telefono = telefono
    #         rh = str(input("Ingrese nuevo rh: "))
    #         data[i -1].rh = rh
    #         eps = str(input("Ingrese nueva eps: "))
    #         data[i -1].eps = eps
    #     elif opt == 2:
    #         newOpt = int(input('\n1-) Crear rutina nueva\n2-) Modificar rutina '))
    #         if newOpt == 1:
    #             # Para crear una nueva rutina
    #             # defino una arreglo o lista vacia del tipo User._historialRutinas
    #             historia:list[User._historialRutinas] = []
    #             #capturo la ultima rutina con el metodo get rutina
    #             if data[i -1].rutina != []:
    #                 ultimaRutina = data[i -1].rutina
    #             ultimaHistoria =  data[i -1].historialRutinas
    #             historia += [ultimaRutina, ultimaHistoria]
    #             # le indico al historial que va a recibir un nuevo arreglo
    #             data[i -1].historialRutinas = historia
    #             # Se niega...
    #             # Creación de la nueva rutina
    #             nIdRutina = int(input("Ingrese el Ide para la rutina"))
    #             nSeries = int(input("Ingrese las series para su nueva rutina"))
    #             nRepeticiones = int(input("Ingrese las repeticiones para su nueva rutina"))
    #             nPeso = int(input("Ingrese el peso para su nueva rutina"))
    #             nHora = int(input("Ingrese la hora de inicio para su rutina"))
    #             nRutina = Routine(nIdRutina, nSeries, nRepeticiones, nPeso, nHora)
    #             data[i -1].rutina = nRutina
    #         elif newOpt == 2:
    #             series = int(input('Ingrese nuevo dato para las series: '))
    #             contador = int(input('Ingrese nuevo dato para el contador: '))
    #             peso = float(input('Ingrese nuevo dato para las peso: '))
    #             tiempo = str(input('Ingrese nuevo dato para las tiempo: '))
    #             data[i -1].rutina = Routine(data[i -1].rutina._routineId, series, contador, peso, tiempo)
    #         else:
    #             print(f"Opcion Incorecta {newOpt}, 1-) Crear Rutina; 2-) Modificar Rutina ")
    #     else:
    #         print(f"Opcion Incorecta {opt}, 1- Modificar Usuario; 2- Modificar Rutina ")
    #         update()
    # def delete():
    #     read()
    #     i = int(input("Ingrese el numero de contacto que desea eliminar: "))
    #     print(f"Estas seguro/a de eliminar a: {data[i-1].nombre} {data[i-1].apellido} con documento {data[i-1].dni}")
    #     resp = str(input("(Y) Borrar - (N) Cancelar: ").lower())
    #     if (resp == 'y'):
    #         #data.remove(data[i -1])
    #         del data[i -1]
    # #Inicio del programa
    # def opciones():
    #     opt:str = ""
    #     while (opt != "x"):
    #         opt = str(input("""  Ingrese una de las siguientes opciones
    # //-----------//-----------//-----------//
    # C-) CREAR NUEVO USUARIO
    # R-) LISTAR USUARIOS
    # U-) MODIFICAR USUARIO
    # D-) ELIMINAR USUARIO
    # X-) SALIR
    # """).lower())
    # #F-) BUSCAR USUARIO
    #         if opt == 'x':
    #             print('Adios')
    #         elif opt == 'c':
    #             create()
    #         elif opt == 'r':
    #             read()
    #         elif opt == 'u':
    #             update()
    #         elif opt == "d":
    #             delete()
    #         else:
    #             print("Opcion incorrecta")
        pass

    # Objetos quemados de Rutinas
    rutinas:list = []
    r1 = Routine(102, 4, 15, 20.0, time(8, 30))
    rutinas.append(r1)
    r2 = Routine(202, 3, 10, 30.0, time(9, 45))
    rutinas.append(r2)
    r3 = Routine(140, 4, 12, 10.0, time(10, 00))
    rutinas.append(r3)
    r4 = Routine(127, 6, 18, 0.0, time(13, 30))
    rutinas.append(r4)
    r5 = Routine(222, 3, 12, 40.0, time(16, 20))
    rutinas.append(r5)
    r6 = Routine(250, 3, 13, 20.5, time(5, 00))
    rutinas.append(r6)
    r7 = Routine(300, 4, 10, 15.0, time(20, 40))
    rutinas.append(r7)


    # Objetos quemados de usuarios
    data:list=[]
    user1 = User("Victor", "Patiño", "13467925-T", "example@yahoo.com", "3010222555", datetime(1994, 3, 13), Rh.O_POSITIVE.value, Eps.SURA.value)
    user1.rutina = r1
    user1.historialRutinas = str(rutinas)
    data.append(user1)
    user2 = User("Julian", "Naranjo", "987654321", "3114445555", "porsospecha@hotmail.com", datetime(2001, 8, 14), Rh.AB_NEGATIVE.value, Eps.SALUDMORTAL.value)
    user2.rutina = r4
    user2.historialRutinas = str(rutinas)
    data.append(user2)
    user3 = User("Sonia", "Herrera", "P-97642585", "3225285746", "profesalveme@yahoo.com", datetime(1961, 12, 31), Rh.O_POSITIVE.value, Eps.ASMETSALUD.value)
    user3.rutina = r7
    user3.historialRutinas = str(rutinas)
    data.append(user3)
    user4 = User("James", "Soto", "1097642585", "3208948576", "aquinoesdonde@gmail.com", datetime(1970, 5, 9), Rh.B_NEGATIVE.value, Eps.ASMETSALUD.value)
    user4.rutina = r5
    user4.historialRutinas = str(rutinas)
    data.append(user4)

    def mergeSort(data):
        
        print(data)
        for e in data:
            print(e.nombre)
        # if len(data) <= 1:
        #     return data
        # medio = len(data) / 2
        # izquierda = data[:medio]
        # derecha = data[medio:]
        # izquierda = mergeSort(izquierda)
        # derecha = mergeSort(derecha)
        # return merge(izquierda, derecha)

    # def merge(listaA, listaB):
    #     global comparaciones
    #     lista_nueva = []
    #     a = 0
    #     b = 0

    #     while a < len(listaA) and b < len(listaB):
    #         comparaciones += 1

    #         if listaA[a] < listaB[b]:
    #             lista_nueva.append(listaA[a])
    #             a += 1
    #         else:
    #             lista_nueva.append(listaB[b])
    #             b += 1

    #     while a < len(listaA):
    #         lista_nueva.append(listaA[a])
    #         a += 1

    #     while b < len(listaB):
    #         lista_nueva.append(listaB[b])
    #         b += 1

    #     return lista_nueva


comparaciones = 0
t0 = time()
arr = mergeSort(data)
t1 = time()
print ("Lista ordenada:")
print (data, "\n")
#print ("Tiempo: {0:f} segundos".format(t1 - t0))
print ("Comparaciones:", comparaciones)