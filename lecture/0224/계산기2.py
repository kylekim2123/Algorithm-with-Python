def change_to_postfix(expression):
    priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
    operators, postfix = [], []
    for token in expression:
        if token.isdigit():
            postfix.append(token)
            continue
        if token == ')':
            while operators[-1] != '(':
                postfix.append(operators.pop())
            operators.pop()
            continue
        if not operators or token == '(' or priority[operators[-1]] < priority[token]:
            operators.append(token)
            continue
        while operators and priority[operators[-1]] >= priority[token]:
            postfix.append(operators.pop())
        operators.append(token)
    if operators:
        postfix.extend(operators[::-1])
    return postfix


def calculate_postfix(expression):
    result = []
    for token in expression:
        if token.isdigit():
            result.append(int(token))
            continue
        b, a = result.pop(), result.pop()
        if token == '+':
            result.append(a + b)
        elif token == '-':
            result.append(a - b)
        elif token == '*':
            result.append(a * b)
        elif token == '/':
            result.append(a / b)
    return result[0]


for t in range(1, 11):
    n = int(input())
    postfix_notation = change_to_postfix(input())
    print('#%s %s' % (t, calculate_postfix(postfix_notation)))
