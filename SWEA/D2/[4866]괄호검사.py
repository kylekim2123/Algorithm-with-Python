# 4866. 괄호검사

def push(v):
    stack.append(v)

def pop():
    if stack:
        return stack.pop()

for t in range(1, int(input())+1):
    sentence = input()
    stack = []
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
        if stack:
            print('#%s 0' % t)
        else:
            print('#%s 1' % t)