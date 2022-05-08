from User import User
from Routine import Routine
from datetime import time, date
from MedicalControl import MedicalControl

if __name__ == '__main__':

    # Objetos quemados de Rutinas
    rutinas:list = []
    r1 = Routine(102, 4, 15, 20.0, time(8, 30), "Acondicionamiento")
    r2 = Routine(202, 3, 10, 30.0, time(9, 45), "Tonificar")
    r3 = Routine(140, 4, 12, 10.0, time(10, 00), "Terapia Fisica")
    r4 = Routine(127, 6, 18, 0.0, time(13, 30), "Terapia Fisica")
    r5 = Routine(222, 3, 12, 40.0, time(16, 20), "Desarrollar")
    r6 = Routine(250, 3, 13, 20.5, time(5, 00), "Tonificar")
    r7 = Routine(300, 4, 10, 15.0, time(20, 40), "Acondicionamiento")
    rutinas = [r1,r2,r3,r4,r5,r6,r7]

    mc_list:list = []
    mC1 = MedicalControl("Dr. Rojas", "Paciente de ingreso, reco: Acondicionamiento", "Rutina: Acondicionamiento Inicial", "1-Sem", date(2022, 5, 7), 0.0, ['A5800','A9645', 'R9865'])
    mC2 = MedicalControl("Dr. Rojas", "Paciente Sin novedad, reco: N/A", "Rutina: libre", "N/A", date(2022, 5, 7), 30.0, ['AB25844','C9634', 'E9865'])
    mC7 = MedicalControl("Dr. Rojas", "Paciente por revisión, reco: N/A", "Rutina: libre", "N/A", date(2022, 5, 7), 30.0, ['AB25844','C9634', 'E9865'])
    mC3 = MedicalControl("Dr. Rojas", "Paciente con mareos, reco: Tonificar", "Rutina: peso medido, fuertes repeticiones", "alternancia", date(2022, 5, 7), 23.5, ['A5248', 'RW961'])
    mC4 = MedicalControl("Dr. Cruz", "Paciente de competencia, reco: N/A", "Rutina: , fuertes repeticiones", "todos los días", date(2022, 5, 7), 15.0, [])
    mC5 = MedicalControl("Dr. Rojas", "Paciente con sobrepeso, reco: Acondicionamiento", "Rutinas poco peso, fuertes repeticiones", "todos los días", date(2022, 5, 7), 8.0, ['R9865'])
    mC6 = MedicalControl("Dr. Cruz", "Paciente con fractura en Femur Izq, reco: Terapia F", "Rutinas poco peso, fuertes repeticiones", "todos los días", date(2022, 5, 7), 3.5, ['A9634'])
    mc_list = [mC1, mC2, mC3 , mC4, mC5, mC6, mC7]
    # Objetos quemados de usuarios
    data:list=[]
    user1 = User("Victor", "Patiño", "13467925-T", "example@yahoo.com", "3010222555", 25, "O+", "Sura", [mC1])
    user1.rutina = r1
    user2 = User("Julian", "Naranjo", "987654321", "3114445555", "porsospecha@hotmail.com", 48, "A-", "Medi+", [mC2,mC7])
    user2.rutina = r4
    user3 = User("Sonia", "Herrera", "P-97642585", "3225285746", "profesalveme@yahoo.com", 33, 'AB+', "Salud Mortal", [mC3, mC4])
    user3.rutina = r7
    user4 = User("James", "Soto", "1097642585", "3208948576", "aquinoesdonde@gmail.com", 21, "O+", "Sanitas", [mC5, mC6])
    user4.rutina = r5
    user5 = User("Aroon", "Smith", "SW-1254873", "3200948006", "itsecurity@itsoft.sw", 21, "O+", "Sura", [])
    user5.rutina = r3
    data = [user1, user2, user3, user4, user5]

 

    

    # def buscarPorEdad():
    #     def binary_search_recursive(data, element, start, end):
    #         if start > end:
    #             return -1

    #         mid = (start + end) // 2
    #         if element == data[mid]:
    #             return mid

    #         if element < data[mid]:
    #             return binary_search_recursive(data, element, start, mid-1)
    #         else:
    #             return binary_search_recursive(data, element, mid+1, end)
        
    #     searchAge = int(input(f"Sobre que edad desea buscar"))
    #     print("Index of {}: {}".format(searchAge, binary_search_recursive(data, searchAge, 0, len(data))))


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
                User.optUsuarios(data)
            elif opt == '2':
                Routine.optRutinas(rutinas)
            # elif opt == '3':
            #     buscarPorEdad()
            #     pass
            else:
                print('Ingreso una opción erronea')
    options()