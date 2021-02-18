# 3143. 가장 빠른 문자열 타이핑

for t in range(1, int(input())+1):
    a, b = input().split()
    typing = a.count(b)
    typing += (len(a) - (typing*len(b)))
    print('#%s %s' % (t, typing))