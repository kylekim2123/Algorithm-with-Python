priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2} # 우선순위
calculator = {'+': lambda x, y: x+y,
              '-': lambda x, y: x-y,
              '*': lambda x, y: x*y,
              '/': lambda x, y: x//y}

def change_to_postfix(expression):
    operators, postfix = [], []
    for token in expression:
        if token.isdigit():
            postfix.append(token) # 피연산자면 바로 push
            continue
        if token == ')': # 닫힌 괄호가 들어오면,
            while operators[-1] != '(':
                postfix.append(operators.pop()) # 열린 괄호가 나올 때까지 연산자를 pop하고 postfix에 push
            operators.pop() # 열린 괄호 제거
            continue
        if not operators or token == '(' or priority[operators[-1]] < priority[token]: # 비었거나, 열린 괄호거나, 우선순위가 높은 연산자이면
            operators.append(token) # 무조건 push
            continue
        while operators and priority[operators[-1]] >= priority[token]: # 우선순위가 낮은 연산자이면, 우선순위가 높아질 때 까지
            postfix.append(operators.pop()) # 연산자에서 pop하여 postfix에 push
        operators.append(token) # 이제 우선순위가 높아졌으므로 해당 연산자 push
    if operators:
        postfix.extend(operators[::-1]) # 연산자가 남아있다면 그대로 postfix에 다 push (순서가 반대이므로 reverse)
    return postfix

def calculate_postfix(expression):
    result = []
    for token in expression:
        if token.isdigit():
            result.append(int(token)) # 피연산자라면 숫자로 변환하고 push
            continue
        b, a = result.pop(), result.pop() # 연산자라면, 두 피연산자 pop하고 연산자에 맞게 연산 (먼저 나오는 피연산자가 b)
        result.append(calculator[token](a, b)) # 딕셔너리의 key로 접근하여 lambda를 이용해 계산하고 push
    return result[0]

for t in range(1, 11):
    n = int(input())
    postfix_notation = change_to_postfix(input()) # 중위표기식 -> 후위표기식
    print('#%s %s' % (t, calculate_postfix(postfix_notation)))
