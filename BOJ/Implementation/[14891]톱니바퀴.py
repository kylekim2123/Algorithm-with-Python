# 14891. 톱니바퀴 (실버1)
def spin(tooth, direction):
    if direction == 1:
        return tooth[-1] + tooth[:-1]
    return tooth[1:] + tooth[0]

saw_tooth = [input(), input(), input(), input()] # 4개의 톱니
k = int(input()) # 회전 횟수
rotations = [list(map(int, input().split())) for _ in range(k)] # 회전 톱니 번호, 방향

count = 0
for rotation in rotations:
    count += 1
    meet = [saw_tooth[0][2] != saw_tooth[1][6], saw_tooth[1][2] != saw_tooth[2][6], saw_tooth[2][2] != saw_tooth[3][6]] # 톱니끼리 맞닿은 부분

    tooth_num, direction = rotation[0]-1, rotation[1]
    saw_tooth[tooth_num] = spin(saw_tooth[tooth_num], direction)
    if tooth_num == 0:
        if meet[0]:
            saw_tooth[1] = spin(saw_tooth[1], -direction)
            if meet[1]:
                saw_tooth[2] = spin(saw_tooth[2], direction)
                if meet[2]:
                    saw_tooth[3] = spin(saw_tooth[3], -direction)
    elif tooth_num == 1:
        if meet[0]:
            saw_tooth[0] = spin(saw_tooth[0], -direction)
        if meet[1]:
            saw_tooth[2] = spin(saw_tooth[2], -direction)
            if meet[2]:
                saw_tooth[3] = spin(saw_tooth[3], direction)
    elif tooth_num == 2:
        if meet[2]:
            saw_tooth[3] = spin(saw_tooth[3], -direction)
        if meet[1]:
            saw_tooth[1] = spin(saw_tooth[1], -direction)
            if meet[0]:
                saw_tooth[0] = spin(saw_tooth[0], direction)
    else:
        if meet[2]:
            saw_tooth[2] = spin(saw_tooth[2], -direction)
            if meet[1]:
                saw_tooth[1] = spin(saw_tooth[1], direction)
                if meet[0]:
                    saw_tooth[0] = spin(saw_tooth[0], -direction)
    
score = int(saw_tooth[0][0]) + int(saw_tooth[1][0])*2 + int(saw_tooth[2][0])*4 + int(saw_tooth[3][0])*8
print(score)