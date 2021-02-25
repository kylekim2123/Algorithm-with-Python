# 3408. 세 가지 합 구하기

for t in range(1, int(input())+1):
    n = int(input())
    s1 = (n//2) + 1 if n % 2 else 0
    s1 += (1+n)*(n//2)
    s3 = s1 + s1
    s2 = s3 - n
    print('#%s %s %s %s' % (t, s1, s2, s3))