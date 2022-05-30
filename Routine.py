from datetime import time
class Routine:
    # Declaracion de Variables
    # cola vacia
    queue:list = []
    # head
    head:int = 0
    # Declaración del constructor
    def __init__(self, routineId:int, series:int, count:int, weight:float, timer:time, bodyzone:str):

        # Datos de entrada
        self._routineId = routineId
        self._series = series
        self._bodyZone = bodyzone
        self._count = count
        self._weight = weight
        self._timer = timer
        self.size = 5

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
        del self._series


    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        self._count = count

    @count.deleter
    def count(self):
        del self._count


    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @weight.deleter
    def weight(self):
        del self._weight


    @property
    def timer(self):
        return self._timer

    @timer.setter
    def timer(self, timer):
        self._timer = timer

    @timer.deleter
    def timer(self):
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

    @property
    def bodyZone(self):
        return self._bodyzone

    @bodyZone.setter
    def bodyZone(self, bodyzone):
        self._bodyzone = bodyzone

    def __str__(self):
        return f"Rutina N° {str(self.routineId)} Compuesta por: {str(self.series)} Series de {str(self.count)} Repeticiones Peso: {str(self.weight)}. Hora: {str(self.timer)}"

    # INICIO marge para rutinas
    def optRutinas(rutinas):
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
        print('\n=======================================================================\n')
        merge_sort(rutinas, 0 , len(rutinas) -1, lambda A, B : A.timer < B.timer)
        print("Rutinas ordenadas por hota inicio: ")
        for r in rutinas:
            print(r)
        print("\n" )

    def enqueue(self, data):
        if (len(self.queue) >= self.size):
            print(f"Queue is Full!!!!")
            result = list(map(lambda x:x, data))
            print(result)
        else:
            input("Ingrese datos de la rutina a encolar")
            routineId = int(input("# Rutina"))
            series = int(input("# Series"))
            count = int(input("# Repeticiones"))
            weight = float(input("Peso en kilos"))
            timer = time(input("Hora"))
            bodyzone = str(input("tipo Rutina"))
            self.e = Routine(routineId, series, count, weight, timer, bodyzone)
            self.queue[:0] = [self.e]
            print(self.queue)

    def dequeue(self):
        if not self.queue:
            print('Queue is Empty!!')
        else:
            self.head = self.queue[-1]
            tem = self.queue[:-1]
            self.queue = tem
            print(f'Element removed: {self.head.routineId}\n{self.head}\n{self.queue}')

    def stack(self):
        temp = self.queue[1:]
        self.queue = temp
        print(f'Element removed: {self.head.routineId}\n{self.head}\n{self.queue}')

