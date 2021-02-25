result = [0]
T = int(input())
for _ in range(1, T+1):
    d, a, b, f = map(int, input().split())
    result.append((d/(a+b))*f)
for t in range(1, T+1):
    print('#%s %f' % (t, result[t]))