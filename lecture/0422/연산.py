MAX = 1000000
OPS = [2, 1, -1, -10]

def bfs(start, end):
    visited = set([start])
    queue = [(start, 0)]
    now = 0
    while now < len(queue):
        x, count = queue[now]
        now += 1
        for op in OPS:
            temp = x * 2 if op == 2 else x + op
            if temp in visited or temp < 1 or temp > MAX:
                continue
            if temp == end:
                return count + 1
            visited.add(temp)
            queue.append((temp, count+1))


for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    print('#%s %s' % (t, bfs(n, m)))