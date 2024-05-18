# 14888. 연산자 끼워넣기 (실버1)


def make_expression(depth, result):
    if depth == n:
        results.append(result)
        return

    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            make_expression(depth + 1, operation[i](result, numbers[depth]))
            operators[i] += 1


n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
operation = {
    0: lambda x, y: x + y,
    1: lambda x, y: x - y,
    2: lambda x, y: x * y,
    3: lambda x, y: -(-x // y) if x < 0 and y > 0 else x // y,
}
results = []

make_expression(1, numbers[0])
print(max(results))
print(min(results))
