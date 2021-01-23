# 1288. 새로운 불면증 치료법

results = list()
for t in range(1, int(input()) + 1):
    n = int(input())
    count = 1
    numbers = set()
    while numbers != {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}:
        sheep = n * count
        digits = list(map(int, list(str(sheep))))
        numbers.update(digits)
        count += 1
    results.append(f'#{t} {sheep}')

for result in results:
    print(result)