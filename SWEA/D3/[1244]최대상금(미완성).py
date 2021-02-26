# 1244. 최대 상금(미완)

# 테스트케이스 32888 해결 필요
def selection_sort(a, n):
    sorted_a = sorted(a,reverse=True)
    turn, i = 0, 0
    while turn < n:
        max_index = i
        for j in range(i+1, len(a)):
            if a[max_index] <= a[j]:
                max_index = j
        if i == max_index or a[i] == a[max_index]:
            if a == sorted_a:
                if len(a) != len(set(a)):
                    turn += 1
                    continue
                a[-1], a[-2] = a[-2], a[-1]
                turn += 1
                continue
            i += 1
            continue
        a[i], a[max_index] = a[max_index], a[i]
        turn += 1

for t in range(1, int(input())+1):
    numbers, n = input().split()
    numbers = list(map(int, numbers))
    selection_sort(numbers, int(n))
    print(f'#{t} {"".join(map(str, numbers))}')
    