# 재귀
def subset(index):
    if index == SIZE:
        if sum(check) == n and k == sum([x+1 for x in range(SIZE) if check[x]]):
            global count
            count += 1
        return
    check[index] = 0
    subset(index+1)
    check[index] = 1
    subset(index+1)


SIZE = 12
for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    check, count = [0]*SIZE, 0
    subset(0)
    print('#%s %s' % (t, count))
