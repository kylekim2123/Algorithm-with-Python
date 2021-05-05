# 10580. 전봇대

for t in range(1, int(input())+1):
    n = int(input())
    lines = [tuple(map(int, input().split())) for _ in range(n)]
    lines.sort()

    total = 0
    for i in range(n):
        for j in range(i+1, n):
            if lines[i][1] > lines[j][1]:
                total += 1
    
    print(f'#{t} {total}')