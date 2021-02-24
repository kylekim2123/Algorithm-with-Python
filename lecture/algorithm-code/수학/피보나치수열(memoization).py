def fibonacci(n):
    # n이 2미만이거나 memo 리스트의 길이보다 작은 경우, 메모한 값에서 꺼내온다
    if n >= 2 and len(memo) <= n:
        memo.append(fibonacci(n-1) + fibonacci(n-2)) # n이 2이상이고 메모에 아직 없다면 새로 해당 값을 메모에 넣는다.
    return memo[n]

memo = [0, 1]
print(fibonacci(10))

# memoization은 이전에 계산한 값을 저장해놓고, 나중에 그 값을 쓸일이 있을 때 다시 계산하지 않고 값을 꺼내오기만 하는 것이다.
# 보통 기초 DP 문제에 사용하게 된다. memoization은 재귀보다는 반복문에 DP를 구현한 것이 더 효율적이다.