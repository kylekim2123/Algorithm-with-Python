# 2628. 종이자르기 (실버5)

n, m = map(int, input().split())
row, col = [0, m], [0, n]

for _ in range(int(input())):
    switch, point = map(int, input().split())
    if switch == 0:
        row.append(point)
    else:
        col.append(point)

row.sort()
col.sort()

areas = [
    (row[i] - row[i - 1]) * (col[j] - col[j - 1])
    for i in range(1, len(row))
    for j in range(1, len(col))
]

print(max(areas))
