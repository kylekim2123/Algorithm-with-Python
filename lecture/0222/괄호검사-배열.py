def push(v):
    global top
    if top < length-1:
        top += 1
        stack[top] = v


def pop():
    global top
    if top >= 0:
        temp = top
        top -= 1
        return stack[temp]


for t in range(1, int(input())+1):
    sentence = input()
    length = len(sentence)
    stack = [''] * length
    top = -1
    for unit in sentence:
        if unit == '(' or unit == '{':
            push(unit)
        elif unit == ')' and pop() != '(':
            print('#%s 0' % t)
            break
        elif unit == '}' and pop() != '{':
            print('#%s 0' % t)
            break
    else:
        if top == -1:
            print('#%s 1' % t)
        else:
            print('#%s 0' % t)
