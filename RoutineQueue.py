class RoutineQueue:
    def __init__(self):
        self.sizeMedicalControl = 5
    # Declaracion de Variables
    # cola vacia
    queue:list = []
    # head
    head:int = 0

    def enqueue(self, data):
        if (len(self.queue) >= self.sizeMedicalControl):
            print(f"Queue is Full!!!!")
        else:
            self.queue[:0] = [data]
            print(self.queue)

    def dequeue(self):
        if not self.queue:
            print('Queue is Empty!!')
        else:
            self.head = self.queue[-1]
            tem = self.queue[:-1]
            self.queue = tem
            print(f'Element removed: {self.head}\n{self.queue}')

    def stack(self):
        if not self.queue:
            print('Queue is Empty!!')
        else:
            temp = self.queue[1:]
            self.queue = temp
            print(f'Element removed: {self.head}\n{self.queue}')