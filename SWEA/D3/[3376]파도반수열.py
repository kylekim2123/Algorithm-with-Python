# 3376. 파도반 수열

for t in range(1, int(input())+1):
    n = int(input())
    if n <= 3:
        print(f'#{t} 1')
        continue
    if n <= 5:
        print(f'#{t} 2')
        continue
    numbers = [1, 1, 1, 2, 2]
    i = 0
    while True:
        numbers.append(numbers[-1]+numbers[i])
        i += 1
        if i == n-5:
            print(f'#{t} {numbers[-1]}')
            break
