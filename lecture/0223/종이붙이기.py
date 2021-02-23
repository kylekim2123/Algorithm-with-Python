def attach(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return attach(n-10) + attach(n-20)*2


for t in range(1, int(input())+1):
    n = int(input())
    print('#%s %s' % (t, attach(n)))