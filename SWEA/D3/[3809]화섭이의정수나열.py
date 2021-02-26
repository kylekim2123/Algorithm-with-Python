# 3809. 화섭이의 정수 나열

for t in range(1, int(input())+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    while len(numbers) != n:
        numbers.extend(list(map(int, input().split())))
    i, j = 10, 1
    while True:
        if i == 10:
            temp1 = set(range(0, i))
        else:
            temp1 = set(range(i//10, i))
        temp2 = set()
        for k in range(0, n-j+1):
            temp2.add(int(''.join(map(str, numbers[k:k+j]))))
        temp3 = temp1 - temp2
        if not temp3:
            i *= 10
            j += 1
        else:
            print(f'#{t} {min(temp3)}')
            break