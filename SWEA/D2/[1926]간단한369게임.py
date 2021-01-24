# 1926. 간단한 369 게임

n = int(input())
for i in range(1, n + 1):
    digits = str(i)
    if ('3' in digits) or ('6' in digits) or ('9' in digits):
        count = digits.count('3') + digits.count('6') + digits.count('9')
        print('-' * count, end=' ')
    else:
        print(i, end=' ')