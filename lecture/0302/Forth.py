operators = {'+', '-', '*', '/'}
calculator = {'+': lambda x, y: x+y,
              '-': lambda x, y: x-y,
              '*': lambda x, y: x*y,
              '/': lambda x, y: x//y}

def forth():
    stack = []
    for unit in postfix:
        if unit.isdigit():
            stack.append(int(unit))
            continue
        if unit in operators:
            if len(stack) < 2:
                return 'error'
            b, a = stack.pop(), stack.pop()
            stack.append(calculator[unit](a, b))
            continue
        if unit == '.':
            if len(stack) > 1:
                return 'error'
            return stack[0]
        return 'error'

for t in range(1, int(input())+1):
    postfix = input().split()
    if (postfix[-1] != '.') or ('.' in postfix[:-1]):
        print('#%s error' % t)
        continue
    print('#%s %s' % (t, forth()))
