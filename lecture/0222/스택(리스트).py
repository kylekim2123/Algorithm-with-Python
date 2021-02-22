stack = []


def push(v):
    stack.append(v)


def pop():
    if stack:
        return stack.pop()
    print('Stack Underflow: pop from empty list')