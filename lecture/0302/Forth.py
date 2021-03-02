operators = {'+', '-', '*', '/'}
calculator = {'+': lambda x, y: x+y,
              '-': lambda x, y: x-y,
              '*': lambda x, y: x*y,
              '/': lambda x, y: x//y}

def forth():
    stack = []
    for unit in postfix:
        if unit.isdigit():
            stack.append(int(unit)) # 숫자면 스택에 push
            continue
        if unit in operators:
            if len(stack) < 2:
                return 'error' # 에러1. 연산자가 너무 많이 입력된 경우
            b, a = stack.pop(), stack.pop()
            stack.append(calculator[unit](a, b)) # 딕셔너리의 key로 접근하여 lambda를 통해 계산
            continue
        if unit == '.':
            if len(stack) > 1:
                return 'error' # 에러2. 마침표가 들어왔는데, 스택에 2개 이상 남아있는 경우
            return stack[0]
        return 'error' # 에러3. "피연산자, 연산자, 마침표" 이외의 값이 입력된 경우

for t in range(1, int(input())+1):
    postfix = input().split()
    if (postfix[-1] != '.') or ('.' in postfix[:-1]):
        print('#%s error' % t) # 에러4. 마지막이 마침표로 끝나지 않거나, 마침표가 앞쪽에서 입력된 경우
        continue
    print('#%s %s' % (t, forth()))
