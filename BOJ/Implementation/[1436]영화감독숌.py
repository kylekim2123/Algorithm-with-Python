# 1436. 영화감독 숌 (실버5)

n = int(input())
start = 666

while n > 1:
    start += 1
    while "666" not in str(start):
        start += 1
    n -= 1

print(start)
