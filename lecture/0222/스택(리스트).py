# 리스트를 이용한 스택 구현

def push(v):
    stack.append(v)


def pop():
    if stack:
        return stack.pop()
    print('Stack Underflow: pop from empty list')


stack = []