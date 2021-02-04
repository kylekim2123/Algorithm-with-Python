# 10202. 문자열 동화

for t in range(1, int(input())+1):
    n = int(input())
    A = input()
    B = input()
    C = input()
    columns = list(zip(A, B, C))

    changes = 0
    for column in columns:
        max_count = max(column.count(column[0]), column.count(column[1])) # 맨 앞과 중간만 보면 된다.
        if max_count == 1:
            changes += 2
        elif max_count == 2:
            changes += 1
    print(f'#{t} {changes}')

            

