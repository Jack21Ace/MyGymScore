from Node import DoublyLinkedList
from User import User
from Routine import Routine
from datetime import time, date
from MedicalControl import MedicalControl

if __name__ == '__main__':

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
    mC1 = MedicalControl("1", "Paciente de ingreso, reco: Acondicionamiento", "Rutina: Acondicionamiento Inicial", "1-Sem", date(2022, 5, 7), 0.0, ['A5800','A9645', 'R9865'])
    mC2 = MedicalControl("2", "Paciente Sin novedad, reco: N/A", "Rutina: libre", "N/A", date(2022, 5, 7), 30.0, ['AB25844','C9634', 'E9865'])
    mC3 = MedicalControl("3", "Paciente con mareos, reco: Tonificar", "Rutina: peso medido, fuertes repeticiones", "alternancia", date(2022, 5, 7), 23.5, ['A5248', 'RW961'])
    mC4 = MedicalControl("4", "Paciente de competencia, reco: N/A", "Rutina: , fuertes repeticiones", "todos los días", date(2022, 5, 7), 15.0, [])
    mC5 = MedicalControl("5", "Paciente con sobrepeso, reco: Acondicionamiento", "Rutinas poco peso, fuertes repeticiones", "todos los días", date(2022, 5, 7), 8.0, ['R9865'])
    mC6 = MedicalControl("6", "Paciente con fractura en Femur Izq, reco: Terapia F", "Rutinas poco peso, fuertes repeticiones", "todos los días", date(2022, 5, 7), 3.5, ['A9634'])
    mC7 = MedicalControl("7", "Paciente por revisión, reco: N/A", "Rutina: libre", "N/A", date(2022, 5, 7), 30.0, ['AB25844','C9634', 'E9865'])
    mc_list = [mC1, mC2, mC3 , mC4, mC5, mC6, mC7]

    data:list=[]
    user1 = User("Victor", "Patiño", "13467925-T", "example@yahoo.com", "3010222555", 25, "O+", "Sura", [mC1])
    # user1.rutina = r1
    user2 = User("Julian", "Naranjo", "987654321", "3114445555", "porsospecha@hotmail.com", 48, "A-", "Medi+", [mC1])
    # user2.rutina = r4
    user3 = User("Sonia", "Herrera", "P-97642585", "3225285746", "profesalveme@yahoo.com", 33, 'AB+', "Salud Mortal", [mC3, mC4])
    # user3.rutina = r7
    user4 = User("James", "Soto", "1097642585", "3208948576", "aquinoesdonde@gmail.com", 21, "O+", "Sanitas", mc_list)
    # user4.rutina = r5
    user5 = User("Aroon", "Smith", "SW-1254873", "3200948006", "itsecurity@itsoft.sw", 21, "O+", "Sura", [])
    # user5.rutina = r3
    data:User = [user1, user2, user3, user4, user5]

    new_linked_list = DoublyLinkedList()
    def options():
        opt = ''
        while (opt != 'x'):
            opt = str(input("Ingrese una de las siguientes opciones\n-----//-----//-----//-----//-----//-----//-----//-----\n1-) Listar elementos\n2-) Insertar al inicio\n3-) Insertar despues de\n4-) Insertar antes de\n5-) Insertar al final\n6-) Eliminar el primero\n7-) Eliminar el ultimo\n8-) Eliminar selección\n9-) Invertir Lista\nX-) Salir\t").lower())
            if opt == 'x':
                print('Bye')
            elif opt == '1':
                print('\tLista Actual\n','----'*7,'\n')
                new_linked_list.traverse_list()
            elif opt == '2':
                if (new_linked_list.start_node == None):
                    e = user1.nombre
                    new_linked_list.insert_in_emptylist(e)
                else:
                    new_linked_list.insert_at_start(e)
            elif opt == '3':
                print('\tLista Actual\n','----'*7,'\n')
                new_linked_list.traverse_list()
                x = input('Despues de que elemento desea insertar')
                e = user2.nombre
                new_linked_list.insert_after_item(x, e)
            elif opt == '4':
                print('\tLista Actual\n','----'*7,'\n')
                new_linked_list.traverse_list()
                x = input('Antes de que elemento desea insertar')
                e = user3.nombre
                new_linked_list.insert_before_item(x, e)
            elif opt == '5':
                print('\tLista Actual\n','----'*7,'\n')
                new_linked_list.traverse_list()
                e = user4.nombre
                new_linked_list.insert_at_end(e)
            elif opt == '6':
                new_linked_list.delete_at_start()
                print('\tLista Actual\n','----'*7,'\n')
                new_linked_list.traverse_list()
            elif opt == '7':
                new_linked_list.delete_at_end
                print('\tLista Actual\n','----'*7,'\n')
                new_linked_list.traverse_list()
            elif opt == '8':
                x = input('que elemento desea Eliminar')
                new_linked_list.delete_element_by_value(x)
                print('\tLista Actual\n','----'*7,'\n')
                new_linked_list.traverse_list()
            elif opt == '9':
                new_linked_list.delete_element_by_value(x)
                print('\tLista Actual\n','----'*7,'\n')
                new_linked_list.reverse_linked_list()
            else:
                print('Opcion incorrecta')
    options()