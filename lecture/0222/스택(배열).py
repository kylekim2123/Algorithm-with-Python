def push1(v):
    global top1
    if top1 == N-1:
        print('Stack Overflow')
        return
    top1 += 1
    stack1[top1] = v


def pop1():
    global top1
    if top1 >= 0:
        temp = top1
        top1 -= 1
        return stack1[temp]
    print('Stack Underflow: pop from empty list')

def push2(v):
    global top2
    if top2 == N:
        print('Stack Overflow')
        return
    stack2[top2] = v
    top2 += 1


def pop2():
    global top2
    if top2 >= 1:
        top2 -= 1
        return stack2[top2]
    print('Stack Underflow: pop from empty list')


N = 3
stack1 = [''] * N
top1 = -1
push1(1)
push1(2)
pop1()
push1(3)
push1(4)
push1(5)
pop1()
pop1()
pop1()
pop1()
print(stack1)

N = 3
stack2 = [''] * N
top2 = 0
push2(1)
push2(2)
pop2()
push2(3)
push2(4)
push2(5)
pop2()
pop2()
pop2()
pop2()
print(stack2)
