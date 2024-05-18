# 1918. 후위 표기식 (골드4)

def change_to_postfix(expression):
    priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
    operators, postfix = [], []
    for token in expression:
        if 65 <= ord(token) <= 90:
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

print(''.join(change_to_postfix(input())))
