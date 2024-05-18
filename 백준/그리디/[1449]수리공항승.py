# 1449. 수리공 항승(실버3)

n, l = map(int, input().split())
holes = list(map(int, input().split()))
holes.sort()
count = 0
for i in range(n):
    if holes[i] == 0:
        continue
    j = i
    possible_range = holes[i] + l - 1
    count += 1
    if possible_range >= holes[n-1]:
        break
    while holes[j] <= possible_range:
        holes[j] = 0
        j += 1

print(count)