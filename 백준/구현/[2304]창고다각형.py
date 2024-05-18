# 2304. 창고 다각형 (실버2)

n = int(input())
pillars = [0] * 1001
for _ in range(n):
    l, h = map(int, input().split())
    pillars[l] = h
for i in range(1000, -1, -1):
    if pillars[i] != 0:
        last = i
        break

max_value = max(pillars)
max_index = pillars.index(max_value)

area, start = 0, 0
for end in range(1, max_index+1):
    if pillars[start] <= pillars[end]:
        area += (end-start) * pillars[start]
        start = end
start = last
for end in range(last-1, max_index-1, -1):
    if pillars[start] <= pillars[end]:
        area += (start-end) * pillars[start]
        start = end
area += max_value
print(area)