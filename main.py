class CircularQueue:
    def __init__(self, size=5):
        self.size = size
        self.queue = [None] * self.size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, value):
        if self.is_full():
            return "Queue is full"
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        return f"Enqueued: {value}"

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        value = self.queue[self.front]
        self.queue[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return f"Dequeued: {value}"

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return f"Front: {self.queue[self.front]}"

    def reverse(self):
        if self.is_empty():
            return "Queue is empty"
        reversed_queue = [None] * self.size
        j = 0
        for i in range(self.rear, self.front - 1, -1):
            reversed_queue[j] = self.queue[i]
            j = (j + 1) % self.size
        self.queue = reversed_queue
        self.front = 0
        self.rear = j - 1
        return "Queue reversed"

    def display(self):
        return self.queue


class SimpleQueue:
    def __init__(self, size=5):
        self.size = size
        self.queue = [None] * self.size
        self.front = 0
        self.rear = -1

    def is_full(self):
        return self.rear == self.size - 1

    def is_empty(self):
        return self.rear < self.front

    def enqueue(self, value):
        if self.is_full():
            return "Queue is full"
        self.rear += 1
        self.queue[self.rear] = value
        return f"Enqueued: {value}"

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        value = self.queue[self.front]
        self.queue[self.front] = None
        self.front += 1
        if self.is_empty():
            self.front = 0
            self.rear = -1
        return f"Dequeued: {value}"

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return f"Front: {self.queue[self.front]}"

    def reverse(self):
        if self.is_empty():
            return "Queue is empty"
        reversed_queue = [None] * self.size
        j = 0
        for i in range(self.rear, self.front - 1, -1):
            reversed_queue[j] = self.queue[i]
            j += 1
        self.queue = reversed_queue
        self.front = 0
        self.rear = j - 1
        return "Queue reversed"

    def display(self):
        return self.queue

    def reset(self):
        self.queue = [None] * self.size
        self.front = 0
        self.rear = -1
        return "Queue reset"


cq = CircularQueue()

print(cq.enqueue(10))  
print(cq.enqueue(20))   
print(cq.enqueue(30))  
print(cq.enqueue(40))  
print(cq.enqueue(50))  
print(cq.dequeue())     
print(cq.peek())        
print(cq.reverse())     
print(cq.display())     

# Testing SimpleQueue
sq = SimpleQueue()

print(sq.enqueue(10))  
print(sq.enqueue(20))  
print(sq.enqueue(30))  
print(sq.enqueue(40))  
print(sq.enqueue(50))  
print(sq.dequeue())     
print(sq.peek())        
print(sq.reverse())     
print(sq.display())     
print(sq.reset())       
print(sq.display())     
