def isEmpty():
    return front == rear

def isFull():
    return (rear+1) % len(cQ) == front

def enQueue(item):
    global rear
    if isFull():
        print('Queue is Full')
        return
    rear = (rear+1) % len(cQ)
    cQ[rear] = item

def deQueue():
    global front
    if isEmpty():
        print('Queue is Empty')
        return
    front = (front+1) % len(cQ)
    return cQ[front]

front, rear = 0, 0
n = 100
cQ = [0] * n