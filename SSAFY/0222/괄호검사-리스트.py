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
            push(unit) # 열린 괄호면 스택에 삽입
        elif unit == ')' and pop() != '(':
            print('#%s 0' % t) # 닫힌 괄호가 나올때, 스택의 마지막 요소가 짝이 맞는 열린 괄호가 아니면, 0을 출력한다.
            break
        elif unit == '}' and pop() != '{':
            print('#%s 0' % t) # 닫힌 괄호가 나올때, 스택의 마지막 요소가 짝이 맞는 열린 괄호가 아니면, 0을 출력한다.
            break
    else:
        if stack:
            print('#%s 0' % t) # input의 끝까지 돌았는데, 괄호가 남아있다면 짝이 맞지 않다는 것이므로 0을 출력한다.
        else:
            print('#%s 1' % t)
