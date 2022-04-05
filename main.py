    # def read(data):
    #     result = list(map(lambda a,b,c,d,e,f,g,h:(a,b,c,d,e,f,g,h), data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
    #     print(result)
from typing import Any
from User import User
from Routine import Routine
from Enums import Eps, Rh
from datetime import time, datetime
from itemCrud import Item
from productCrud import Product
from SupplierCrud import Proveedor

if __name__ == '__main__':

    def optUser():
        def create():
            nombre = str(input("Ingrese nombre: "))
            apellido = str(input("Ingrese apellido: "))
            dni = str(input("Ingrese dni: "))
            email = str(input("Ingrese email: "))
            fechNacimiento = str(input("Ingrese fechNacimiento: "))
            telefono = str(input("Ingrese telefono: "))
            rh = str(input("Ingrese rh: "))
            eps = str(input("Ingrese eps: "))
            nuevoUsuario = User(nombre, apellido, dni, email, fechNacimiento, telefono, rh, eps)
            data.append(nuevoUsuario)

        def read():
            print("-------Lista de Usuarios-------\n")
            for i in range(0, len(data)):
                print(f"{i+1}-)\n{data[i]}")

        def update():
            read()
            i = int(input("Ingrese el numero de contacto que desea Modificar: "))
            opt = int(input("1-) Modificar Dtos Usuario\n2-) Modificar Dtos Rutina "))
            if opt == 1:
                nombre = str(input("Ingrese nuevo Nombre: "))
                data[i -1].nombre = nombre
                apellido = str(input("Ingrese nuevo Apellido: "))
                data[i -1].apellido = apellido
                dni = str(input("Ingrese nuevo DNI: "))
                data[i -1].dni = dni
                email = str(input("Ingrese nuevo Correo: "))
                data[i -1].email = email
                fechaNaci = str(input("Ingrese nueva Fecha Nacimiento: "))
                data[i -1].fechaNacimiento = fechaNaci
                telefono = str(input("Ingrese nuevo Telefono: "))
                data[i -1].telefono = telefono
                rh = str(input("Ingrese nuevo rh: "))
                data[i -1].rh = rh
                eps = str(input("Ingrese nueva eps: "))
                data[i -1].eps = eps
            elif opt == 2:
                newOpt = int(input('\n1-) Crear rutina nueva\n2-) Modificar rutina '))
                if newOpt == 1:
                    # Para crear una nueva rutina
                    # defino una arreglo o lista vacia del tipo User._historialRutinas
                    historia:list[User._historialRutinas] = []
                    #capturo la ultima rutina con el metodo get rutina
                    if data[i -1].rutina != []:
                        ultimaRutina = data[i -1].rutina
                    ultimaHistoria =  data[i -1].historialRutinas
                    historia += [ultimaRutina, ultimaHistoria]
                    # le indico al historial que va a recibir un nuevo arreglo
                    data[i -1].historialRutinas = historia
                    # Se niega...

                    # Creación de la nueva rutina
                    nIdRutina = int(input("Ingrese el Ide para la rutina"))
                    nSeries = int(input("Ingrese las series para su nueva rutina"))
                    nRepeticiones = int(input("Ingrese las repeticiones para su nueva rutina"))
                    nPeso = int(input("Ingrese el peso para su nueva rutina"))
                    nHora = int(input("Ingrese la hora de inicio para su rutina"))
                    nRutina = Routine(nIdRutina, nSeries, nRepeticiones, nPeso, nHora)
                    data[i -1].rutina = nRutina
                elif newOpt == 2:
                    series = int(input('Ingrese nuevo dato para las series: '))
                    contador = int(input('Ingrese nuevo dato para el contador: '))
                    peso = float(input('Ingrese nuevo dato para las peso: '))
                    tiempo = str(input('Ingrese nuevo dato para las tiempo: '))
                    data[i -1].rutina = Routine(data[i -1].rutina._routineId, series, contador, peso, tiempo)
                else:
                    print(f"Opcion Incorecta {newOpt}, 1-) Crear Rutina; 2-) Modificar Rutina ")
            else:
                print(f"Opcion Incorecta {opt}, 1- Modificar Usuario; 2- Modificar Rutina ")
                update()

        def delete():
            read()
            i = int(input("Ingrese el numero de contacto que desea eliminar: "))
            print(f"Estas seguro/a de eliminar a: {data[i-1].nombre} {data[i-1].apellido} con documento {data[i-1].dni}")
            resp = str(input("(Y) Borrar - (N) Cancelar: ").lower())
            if (resp == 'y'):
                #data.remove(data[i -1])
                del data[i -1]

        #Inicio del programa
        def opciones():
            opt:str = ""
            while (opt != "x"):
                opt = str(input("""  Ingrese una de las siguientes opciones
        //-----------//-----------//-----------//
        C-) CREAR NUEVO USUARIO
        R-) LISTAR USUARIOS
        U-) MODIFICAR USUARIO
        D-) ELIMINAR USUARIO
        X-) SALIR
        """).lower())
        #F-) BUSCAR USUARIO

                if opt == 'x':
                    print('Adios')
                elif opt == 'c':
                    create()
                elif opt == 'r':
                    read()
                elif opt == 'u':
                    update()
                elif opt == "d":
                    delete()
                else:
                    print("Opcion incorrecta")

        data:list=[]
        # Objetos quemados de Rutinas
        rutinas:list = []
        r1 = Routine(102, 4, 15, 20.0, time(8, 30))
        rutinas.append(r1.__str__())
        r2 = Routine(202, 3, 10, 30.0, time(9, 45))
        rutinas.append(r2.__str__())
        r3 = Routine(140, 4, 12, 10.0, time(10, 00))
        rutinas.append(r3.__str__())
        r4 = Routine(127, 6, 18, 0.0, time(13, 30))
        rutinas.append(r4.__str__())
        r5 = Routine(222, 3, 12, 40.0, time(16, 20))
        rutinas.append(r5.__str__())
        r6 = Routine(250, 3, 13, 20.5, time(5, 00))
        rutinas.append(r6.__str__())
        r7 = Routine(300, 4, 10, 15.0, time(20, 40))
        rutinas.append(r7.__str__())

        # Objetos quemados de usuarios
        user1 = User("Victor", "Patiño", "13467925-T", "example@yahoo.com", '13 de marzo de 1994', 3010222555, Rh.O_POSITIVE.value, Eps.SURA.value)
        user1.rutina = r1
        user1.historialRutinas = str(rutinas)
        data.append(user1)
        user2 = User("Julian", "Naranjo", "987654321", "porsospecha@hotmail.com", 3114445555, "14 de agosto de 2001", Rh.AB_NEGATIVE.value, Eps.SALUDMORTAL.value)
        user2.rutina = r4
        user2.historialRutinas = str(rutinas)
        data.append(user2)
        user3 = User("Sonia", "Herrera", "P-97642585", "profesalveme@yahoo.com", 3225285746, "31 de diciembre de 1961", Rh.O_POSITIVE.value, Eps.ASMETSALUD.value)
        user3.rutina = r7
        user3.historialRutinas = str(rutinas)
        data.append(user3)
        user4 = User("James", "Soto", "1097642585", "aquinoesdonde@gmail.com", 3208948576, "9 de mayo de 1970", Rh.B_NEGATIVE.value, Eps.ASMETSALUD.value)
        user4.rutina = r5
        user4.historialRutinas = str(rutinas)
        data.append(user4)

        opciones()

    def optItem():
        def agregar(): # funcion o metodo
            iditem = int(input("Ingrese el id del item: "))
            nombre = str(input("ingrese el nombre del item: "))
            monto = float(input("ingrese el monto: "))
            estado = bool(input("Si- True - No - False: "))
            descripcion =str(input("ingrese la descripcion: "))
            tipo = type (input ("ingrese el tipo: "))
            proveedor = input ("ingrese el proveedor: ")
            itemNuevo = Item(iditem,nombre,monto,estado,descripcion,tipo,proveedor)
            listaItem.append(itemNuevo)#append lo que hace es agragar en la cola el nuevo dato , depes del ultimo elemento + 1
            #print(itemNuevo)

        def informar():
            print("")
            print("-----informe-----")
            for indice in range(0, len(listaItem)):
                print(f"{indice +1} - {listaItem[indice]}")

        def borrar():
            informar()
            indice =int(input("Ingrese el numero  de item que desea eliminar: "))
            print(f"Esta seguro/a de eliminar a {listaItem[indice -1].getNombre()} {listaItem[indice -1].getMonto()}")
            respuesta = input("S- Borrar - N - No borrar ")
            if (respuesta == "s"):
                listaItem.remove(listaItem[indice -1])

        def modificar():
                informar()
                indice =int(input("Ingrese el numero de item que desea modificar: "))
                nombre = input("ingrese nuevo nombre: ")
                listaItem[indice -1].setNombre(nombre)
                monto = input("ingrese nuevo monto: ")
                listaItem[indice -1].setMonto(monto)
                estado = input("ingrese nuevo estado: ")
                listaItem[indice -1].setEstado(estado)
                descripcion = input("ingresie nueva descripción: ")
                listaItem[indice -1].setDescripcion(descripcion)
                tipo = input("ingrese nuevo tipo: ")
                listaItem[indice -1].setTipo(tipo)
                proveedor = input("ingrese nuevo proveedor: ")
                listaItem[indice -1].setProveedor(proveedor)

        #Inicio del programa
        listaItem = []
        item1=Item('1','Colchoneta','2','activo','Ejercicios ABS','Stool','Jisus')
        item2=Item('2','balones','10','activo','Ejercicios ','Stool','adidas')
        listaItem.append(item1)
        listaItem.append(item2)
        opcion = ' '
        while(opcion != 'x'):
            print("--------------------------------")
            print("1 - Agregar Item")
            print("2 - Modificar Item")
            print("3 - Mostrar Item")
            print("4 - Borrar item")
            print("x - Salir")
            opcion = input("ingrese la opcion deseada: ")
            if(opcion == "x"):
                print("Saliendo...")
            elif(opcion == '1'):
                agregar()
            elif(opcion == '3'):
                informar()
            elif(opcion == '4'):
                borrar()
            elif(opcion == '2'):
                modificar() 
            else:
                print("Opcion incorrecta")

    def optProducto():
        def agregar(): # funcion o metodo
            productId =int(input("Ingrese el id del producto: "))
            productNombre = str(input("ingrese el nombre del producto: "))
            precio = float(input("ingrese el precio: "))
            marca = str(input("ingresa la marca: "))
            vencimiento =str(input("ingrese el vencimiento  "))
            disponible = bool(input("Si- True - No - False: "))
            proveedor = str(input("ingrese el proveedor: "))
            productNuevo = Product(productId,productNombre,precio,marca,vencimiento,disponible,proveedor)
            listaProduct.append(productNuevo)#append lo que hace es agragar en la cola el nuevo dato , depes del ultimo elemento + 1
            #print(itemNuevo)

        def informar():
            print("")
            print("-----informe-----")
            for indice in range(0, len(listaProduct)):
                print(f"{indice +1} - {listaProduct[indice]}")

        def borrar():
            informar()
            indice =int(input("Ingrese el numero  de item que desea eliminar: "))
            print(f"Esta seguro/a de eliminar a {listaProduct[indice -1].getProductNombre()} {listaProduct[indice -1].getPrecio()}")
            respuesta = input("S- Borrar - N - No borrar ")
            if (respuesta == "s"):
                listaProduct.remove(listaProduct[indice -1])

        def modificar():
            informar()
            indice =int(input("Ingrese el numero de producto que desea modificar: "))
            productNombre = input("ingrese nuevo nombre producto: ")
            listaProduct[indice -1].setProductNombre(productNombre)
            precio= input("ingrese nuevo precio: ")
            listaProduct[indice -1].setPrecio(precio)
            marca = input("ingrese nuevo marca: ")
            listaProduct[indice -1].setMarca(marca)
            vencimiento = input("ingresie nuevo  fecha de vencimiento:  ")
            listaProduct[indice -1].setVencimiento(vencimiento)
            disponible = input("ingreso la validación: " )
            listaProduct[indice -1].setDisponible(disponible)
            proveedor = input("ingrese nuevo proveedor: ")
            listaProduct[indice -1].setProveedor(proveedor)

        #Inicio del programa
        listaProduct = []
        product1 = Product(1,'cc',0.1,'col', datetime(2023,3,12),True,Any)
        product2= Product(2,'cmc',5.1,'cool', datetime(2023,3,12),True,Any)
        listaProduct.append(product1)
        listaProduct.append(product2)
        opcion = ' '
        while(opcion != 'x'):
            print("--------------------------------")
            print("1 - Agregar Item")
            print("2 - Modificar Item")
            print("3 - Mostrar Item")
            print("4 - Borrar item")
            print("x - Salir")
            opcion = input("ingrese la opcion deseada: ")
            if(opcion == "x"):
                print("Saliendo...")
            elif(opcion == '1'):
                agregar()
            elif(opcion == '3'):
                informar()
            elif(opcion == '4'):
                borrar()
            elif(opcion == '2'):
                modificar() 
            else:
                print("Opcion incorrecta")

    def optProveedor():
        def agregar(): # funcion o metodo
            nit = int(input("Ingrese el Nit: "))
            nombre = str(input("ingrese el nombre del proveedor: "))
            telefono = str(input("ingrese el numero telefonico: "))
            correo = str(input("Ingrese el correo electronico"))
            itemNuevo = Proveedor(nit,nombre,telefono,correo)
            listaItem.append(itemNuevo)#append lo que hace es agragar en la cola el nuevo dato , depes del ultimo elemento + 1
            #print(itemNuevo)

        def informar():
            print("")
            print("-----informe-----")
            for indice in range(0, len(listaItem)):
                print(f"{indice +1} - {listaItem[indice]}")

        def borrar():
            informar()
            indice =int(input("Ingrese el numero  de item que desea eliminar: "))
            print(f"Esta seguro/a de eliminar a {listaItem[indice -1].getNombre()} {listaItem[indice -1].getTelefono()} {listaItem[indice -1].getCorreo()}")
            respuesta = input("S- Borrar - N - No borrar ")
            if (respuesta == "s"):
                listaItem.remove(listaItem[indice -1])

        def modificar():
                informar()
                indice =int(input("Ingrese el numero de item que desea modificar: "))
                nombre = input("ingrese nuevo nombre: ")
                listaItem[indice -1].setNombre(nombre)
                telefono = input("ingrese nuevo telefono: ")
                listaItem[indice -1].setTelefono(telefono)
                correo = input("ingrese nuevo correo: ")
                listaItem[indice -1].setCorreo(correo)

        #Inicio del programa
        listaItem = []
        item1=Proveedor(895053265,"COlCALDAS","3205437504","caldas@gmail.com")
        item2=Proveedor(895052665,"COl","32054315204","cals@gmail.com")
        item3=Proveedor(895053265,"COlCALDAS","3205437504","caldas@gmail.com")
        item4=Proveedor(895052665,"COl","32054315204","cals@gmail.com")
        item5=Proveedor(895053265,"COlCALDAS","3205437504","caldas@gmail.com")
        item6=Proveedor(895052665,"COl","32054315204","cals@gmail.com")
        listaItem.append(item1)
        listaItem.append(item2)
        listaItem.append(item3)
        listaItem.append(item4)
        listaItem.append(item5)
        listaItem.append(item6)

        # def particionado(listaItem):
        #     pivote = listaItem[0]
        #     menores = []
        #     mayores = []

        #     for i in listaItem:
        #         if listaItem[i][0] < pivote:
        #             menores.append(listaItem[i])
        #         else:
        #             mayores.append(listaItem[i])
        #     return menores, pivote, mayores

        # def quicksort (listaItem):
        #     if len(listaItem)<2:
        #         return listaItem
        #     menores, pivote, mayores = particionado(listaItem)
        #     return  quicksort(menores) + [pivote] + quicksort(mayores)

        # print(quicksort(listaItem))

        opcion = ' '
        while(opcion != 'x'):
            print("--------------------------------")
            print("1 - Agregar Item")
            print("2 - Modificar Item")
            print("3 - Mostrar Item")
            print("4 - Borrar item")
            print("x - Salir")
            opcion = input("ingrese la opcion deseada: ")
            if(opcion == "x"):
                print("Saliendo...")
            elif(opcion == '1'):
                agregar()
            elif(opcion == '3'):
                informar()
            elif(opcion == '4'):
                borrar()
            elif(opcion == '2'):
                modificar() 
            else:
                print("Opcion incorrecta")


    def menu():
        opt:str = ""
        while (opt != "x"):
            opt = str(input("""  Ingrese una de las siguientes opciones
    //-----------//-----------//-----------//
    1-) MODULO USUARIO
    2-) MODULO ITEMS
    3-) MODULO PROVEEDORES
    4-) MODULO PRODUCTOS
    0-) SALIR
    """).lower())
    #F-) BUSCAR USUARIO
            if opt == '0':
                print('Adios')
                break
            elif opt == '1':
                optUser()
            elif opt == '2':
                optItem()
            elif opt == '3':
                optProveedor()
            elif opt == "4":
                optProducto()
            else:
                print("Opcion incorrecta")
    menu()