def isFull():
    return rear == n-1 # 꼬리가 맨 끝에 도달하면 Queue가 가득찬 것

def isEmpty():
    return front == rear # 머리와 꼬리가 만나면 Queue가 빈 것

def enQueue(q, data):
    global rear
    if isFull():
        print('Queue is full')
        return
    rear += 1
    q[rear] = data

def deQueue(q):
    global front
    if isEmpty():
        print('Queue is empty')
        return
    front += 1
    return q[front]

for t in range(1, int(input())+1):
    numbers = input().split()
    n = len(numbers)
    front = rear = -1
    queue = [0] * n
    for number in numbers:
         enQueue(queue, number)
    print('#%s' % t, deQueue(queue), deQueue(queue), deQueue(queue))
