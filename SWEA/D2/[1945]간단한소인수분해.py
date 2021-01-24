# 1945. 간단한 소인수분해

results = list()
for t in range(1, int(input()) + 1):
    number = int(input())
    exponent = [0, 0, 0, 0, 0] # 순서대로 a, b, c, d, e
    factors = [2, 3, 5, 7, 11]
    for factor in factors:
        while number % factor == 0:
            number //= factor
            exponent[factors.index(factor)] += 1 

    results.append(exponent)

count = 1
for result in results:
    print(f'#{count}', end=' ')
    print(*result)
    count += 1