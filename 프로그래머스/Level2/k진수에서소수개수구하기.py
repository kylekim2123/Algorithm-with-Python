# 2022 KAKAO BLIND RECRUITMENT k진수에서 소수 개수 구하기 (Level 2)


def convert(n, k):
    result = ""

    while n > 0:
        n, mod = divmod(n, k)
        result += str(mod)

    return result[::-1]


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** (0.5)) + 1):
        if n % i == 0:
            return False

    return True


def solution(n, k):
    n = str(n) if k == 10 else convert(n, k)
    numbers = [i for i in n.split("0") if i and is_prime(int(i))]
    
    return len(numbers)
