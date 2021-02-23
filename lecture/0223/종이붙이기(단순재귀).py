# 단순 재귀로 구현 (중복 연산 많음)
def attach(n):
    if n < 0:
        return 0 # n이 0보다 작다는 것은 더이상 붙일 곳이 없다는 것이므로 0을 반환
    if n == 0:
        return 1 # n이 0이라는 것은 하나를 붙여서 이제 남은 곳이 없다는 것이므로 1을 반환
    return attach(n-10) + attach(n-20)*2 # 10짜리를 붙였을 때 + (20짜리를 붙였을때 * 2)
    # -> 20짜리가 두개인 이유는 10짜리를 눕혀서 붙이는 경우도 있기 때문


for t in range(1, int(input())+1):
    n = int(input())
    print('#%s %s' % (t, attach(n)))