# 3131. 100만 이하의 모든 소수

# 에라토스테네스의 체
number = [i for i in range(1000001)]
for i in range(2, 1000001):
    if number[i] == 0:
        continue
    for j in range(i+i, 1000001, i):
        number[j] = 0

for i in range(2, 1000001):
    if number[i] != 0:
        print(number[i], end=' ')
    