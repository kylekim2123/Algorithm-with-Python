# Memoization 이용해서 구현 (중복 계산 줄임)
def attach(n):
    if n > 2 and len(memo) < n:
        memo.append(attach(n-1) + attach(n-2)*2)
    return memo[n-1]


for t in range(1, int(input())+1):
    n = int(input()) // 10
    memo = [1, 3]
    print('#%s %s' % (t, attach(n)))
