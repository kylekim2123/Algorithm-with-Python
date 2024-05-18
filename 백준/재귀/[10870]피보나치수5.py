# 10870. 피보나치 수 5 (브론즈2)


def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 2) + fibonacci(number - 1)


print(fibonacci(int(input())))
