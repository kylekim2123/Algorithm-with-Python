# 1100. 하얀 칸 (브론즈 2)

chess_board = [list(input()) for _ in range(8)]
cnt = -1
white = 0
for i in chess_board:
    for j in i:
        cnt += 1
        if cnt % 2 == 0:
            if j == "F":
                white += 1
    cnt += 1
print(white)
