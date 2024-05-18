# 1. 근묵자흑

n, k = map(int, input().split())
numbers = list(map(int, input().split()))
min_number = min(numbers)
min_index = numbers.index(min_number)

start = min_index - (k-1)
if start < 0:
    start = 0

min_count = n
while start <= min_index:
    end = start + (k-1)
    count = 1
    i, j = start, end
    while i > 0:
        count += 1
        i -= (k-1)
    while j < n-1:
        count += 1
        j += (k-1)
    min_count = min(min_count, count)
    start += 1
print(min_count)