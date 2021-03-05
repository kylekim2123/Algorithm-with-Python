# 10872. 팩토리얼 (브론즈3)

def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number-1)

n = int(input())
print(factorial(n))
