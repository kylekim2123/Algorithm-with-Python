# 10870. 피보나치 수 5 (브론즈2)

def fibo(number):
    if number >= 2 and len(memo) <= number:
        memo.append(fibo(number-1) + fibo(number-2))
    return memo[number]

n = int(input())
memo = [0, 1]
print(fibo(n))
