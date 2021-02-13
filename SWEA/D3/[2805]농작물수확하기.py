# 2805. 농작물 수확하기

for t in range(1, int(input())+1):
    n = int(input())
    total = 0
    switch = False
    index = n // 2
    jump = 1
    for i in range(n):
        line = list(map(int, list(input())))
        total += sum(line[index:index+jump])
        if i == n//2:
            switch = True
        if switch:
            jump -= 2
            index += 1
        else:
            jump += 2
            index -= 1
    print(f'#{t} {total}')