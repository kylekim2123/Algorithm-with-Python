# 14719. 빗물 (골드5)
h, w = map(int, input().split())
blocks = list(map(int, input().split()))

water = 0
standard = 0
for i in range(w):
    if blocks[standard] > blocks[i]:
        for j in range(standard+1, i):
            if blocks[i] > blocks[j]:
                water += blocks[i] - blocks[j]
                blocks[j] += blocks[i] - blocks[j]
    else:
        for j in range(standard+1, i):
            water += blocks[standard] - blocks[j]
            blocks[j] += blocks[standard] - blocks[j]
        standard = i

print(water)