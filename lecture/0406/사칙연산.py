# 사칙연산을 위한 람다 함수 모음
CALCULATION = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y
}

def calculate(index):
    node = tree[index]
    if len(node) > 1: # 연산자가 들어있는 곳은 길이가 1이 넘고, 피연산자만 들어있는 곳은 길이가 1이다.
        left, right = calculate(int(node[1])), calculate(int(node[2])) # 후위탐색을 통해 left, right 서브트리 값을 계산해서 담는다.
        return CALCULATION[node[0]](left, right) # 연산자에 맞게 연산하여 그 결과값을 반환
    return int(node[0]) # 피연산자만 들어있는 노드라면 그냥 값만 반환

for t in range(1, 11):
    n = int(input())
    tree = [0] + [input().split()[1:] for _ in range(n)]
    print('#%s %s' % (t, calculate(1)))