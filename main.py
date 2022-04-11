from collections import namedtuple
from operator import attrgetter
from User import User
from Routine import Routine
from Enums import Eps, Rh
from datetime import time
# from itemCrud import Item
# from productCrud import Product
# from SupplierCrud import Proveedor
# from GymCrud import Gym
# from CampusCrud import Campus

if __name__ == '__main__':

    # Objetos quemados de Rutinas
    rutinas:list = []
    r1 = Routine(102, 4, 15, 20.0, time(8, 30))
    r2 = Routine(202, 3, 10, 30.0, time(9, 45))
    r3 = Routine(140, 4, 12, 10.0, time(10, 00))
    r4 = Routine(127, 6, 18, 0.0, time(13, 30))
    r5 = Routine(222, 3, 12, 40.0, time(16, 20))
    r6 = Routine(250, 3, 13, 20.5, time(5, 00))
    r7 = Routine(300, 4, 10, 15.0, time(20, 40))
    rutinas = [r1,r2,r3,r4,r5,r6,r7]


    # Objetos quemados de usuarios
    data:list=[]
    user1 = User("Victor", "Patiño", "13467925-T", "example@yahoo.com", "3010222555", 25, Rh.O_POSITIVE.value, Eps.SURA.value)
    user1.rutina = r1
    #user1.historialRutinas = rutinas
    user2 = User("Julian", "Naranjo", "987654321", "3114445555", "porsospecha@hotmail.com", 48, Rh.AB_NEGATIVE.value, Eps.SALUDMORTAL.value)
    user2.rutina = r4
    #user2.historialRutinas = rutinas
    user3 = User("Sonia", "Herrera", "P-97642585", "3225285746", "profesalveme@yahoo.com", 33, Rh.O_POSITIVE.value, Eps.ASMETSALUD.value)
    user3.rutina = r7
    #user3.historialRutinas = rutinas
    user4 = User("James", "Soto", "1097642585", "3208948576", "aquinoesdonde@gmail.com", 21, Rh.B_NEGATIVE.value, Eps.ASMETSALUD.value)
    user4.rutina = r5
    #user4.historialRutinas = rutinas 
    data = [user1, user2, user3, user4]

    # INICIO quick sort para usuarios
    def optUsuarios():
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
    
    # INICIO marge para rutinas
    def optRutinas():
        def merge(rutinas, leftIndex, rightIndex, middle, compare_func):
            leftCopy = rutinas[leftIndex:middle + 1]
            rightCopy = rutinas[middle+1:rightIndex+1]
            leftCopyIndex = 0
            rightCopyIndex = 0
            sortedIndex = leftIndex
            while leftCopyIndex < len(leftCopy) and rightCopyIndex < len(rightCopy):
                if compare_func(leftCopy[leftCopyIndex], rightCopy[rightCopyIndex]):
                    rutinas[sortedIndex] = leftCopy[leftCopyIndex]
                    leftCopyIndex += 1
                else:
                    rutinas[sortedIndex] = rightCopy[rightCopyIndex]
                    rightCopyIndex += 1
                sortedIndex = sortedIndex + 1
            while leftCopyIndex < len(leftCopy):
                rutinas[sortedIndex] = leftCopy[leftCopyIndex]
                leftCopyIndex += 1
                sortedIndex += 1
            while rightCopyIndex < len(rightCopy):
                rutinas[sortedIndex] = rightCopy[rightCopyIndex]
                rightCopyIndex += 1
                sortedIndex += 1
        def merge_sort(rutinas, leftIndex, rightIndex, compare_func):
            if leftIndex >= rightIndex:
                return
            middle = (leftIndex + rightIndex)//2
            merge_sort(rutinas, leftIndex, middle, compare_func)
            merge_sort(rutinas, middle + 1, rightIndex, compare_func)
            merge(rutinas, leftIndex, rightIndex, middle, compare_func)

        merge_sort(rutinas, 0 , len(rutinas)-1, lambda A, B : A.series < B.series)
        print("rutinas ordenadas por Series: ")
        for s in rutinas:
            print(s)
        print('\n=======================================================================\n')
        merge_sort(rutinas, 0 , len(rutinas) -1, lambda A, B : A.timer < B.timer)
        print("rutinas ordenadas por hota inicio: ")
        for r in rutinas:
            print(r)
    

    def buscarPorEdad():
        def binary_search_recursive(data, element, start, end):
            if start > end:
                return -1

            mid = (start + end) // 2
            if element == data[mid]:
                return mid

            if element < data[mid]:
                return binary_search_recursive(data, element, start, mid-1)
            else:
                return binary_search_recursive(data, element, mid+1, end)
        
        searchAge = int(input(f"Sobre que edad desea buscar"))
        print("Index of {}: {}".format(searchAge, binary_search_recursive(data, searchAge, 0, len(data))))


        # def find_index(elements, value, key=lambda x: x):
        #     ...

        # # def contains(elements, value, key=lambda x: x):
        # #     return find_index(elements, value, key=lambda x: x) is not None

        # def find(elements, value, key=lambda x: x):
        #     index = find_index(elements, value, key)
        #     return None if index is None else elements[index]
        

        # find(data, key=lambda x : x.edad, value=33)

    def options():
        opt = ''
        while (opt != 'x'):
            opt = str(input("Ingrese una de las siguientes opciones\n-----//-----//-----//-----//-----//-----//-----//-----\n1-) Ordenar por Usuarios\n2-) Ordenar por Rutinas\n3-) Buscar Usuario por Edad\nX-) Salir\n").lower())
            if opt == 'x':
                print('Adios')
            elif opt == '1':
                optUsuarios()
            elif opt == '2':
                optRutinas()
            elif opt == '3':
                buscarPorEdad()
                pass
            else:
                print('Ingreso una opción erronea')
    options()