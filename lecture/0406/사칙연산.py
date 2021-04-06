CALCULATION = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y
}

def calculate(index):
    node = tree[index]
    if len(node) > 1:
        left, right = calculate(int(node[1])), calculate(int(node[2]))
        return CALCULATION[node[0]](left, right)
    return int(node[0])

for t in range(1, 11):
    n = int(input())
    tree = [0] + [input().split()[1:] for _ in range(n)]
    print('#%s %s' % (t, calculate(1)))