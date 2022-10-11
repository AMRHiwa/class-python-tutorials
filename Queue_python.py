
class Queue:
    def __init__(self, k) -> None:
        self.k = k
        self.queue = [None] * k
        self.front = -1
        self.rear = -1

    def display(self):
        for i in range(self.front, self.rear+1):
            print(self.queue[i], end="\t")
        print()

    def enqueue(self, data):
        if ((self.rear + 1) == self.k) :
            print("Queue is Full")
        
        elif (self.front == -1):
            self.rear = 0
            self.front = 0
            self.queue[self.rear] = data

        else:
            self.rear += 1
            self.queue[self.rear] = data
    
    def dequeue(self):
        if (self.front == -1):
            print("Queue is empty")
        elif self.front == self.rear:
            t = self.queue[self.front]
            self.queue[self.front] = None
            self.rear = -1
            self.front = -1
            return t
        else:
            t = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1
            return t

f_1 = Queue(5)
f_1.enqueue('Hiwa')
f_1.enqueue("Mohamad")
f_1.enqueue("Khalil")
f_1.display()
a = f_1.dequeue()
print(a)
f_1.display()