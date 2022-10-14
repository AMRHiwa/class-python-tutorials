class RotaryQueue:
    def __init__(self, k) -> None:
        self.k = k
        self.queue = [None] * k
        self.front = -1
        self.rear = -1
    
    def display(self):
        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end="\t")
        print()

    def enqueue(self, data):
        if ((self.rear + 1) % self.k) == self.front:
            print("Queue is Full")
        elif self.rear == self.front:
            self.rear += 1
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.k
            self.queue[self.rear] = data
    
    def dequeue(self):
        if self.rear == -1:
            print("Queue is Empty")
            return

        elif self.rear == self.front:
            t = self.queue[self.front]
            self.rear = -1
            self.front = -1
            return t

        else:
            t = self.queue[self.front]
            self.front = (self.front + 1 ) % self.k
