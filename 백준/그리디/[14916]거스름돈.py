# 14916. 거스름돈(실버5)

n = int(input())
if n == 1 or n == 3:
    print(-1)
else:
    count = 0
    last_number = int(str(n)[-1])
    if last_number == 1 or last_number == 6:
        n -= 6
        count += 3
    elif last_number == 3 or last_number == 8:
        n -= 8
        count += 4
    count += n // 5
    n %= 5
    count += n // 2
    n %= 2
    print(count)

        
