# 2828. 사과 담기 게임(브론즈1)

n, m = map(int, input().split()) # n : 스크린의 칸 / m : 바구니의 길이
left_m = 1
right_m = m 

count = 0
for _ in range(int(input())):
    apple = int(input())
    if apple < left_m:
        moving_left = left_m - apple
        count += moving_left
        left_m -= moving_left
        right_m -= moving_left
    elif apple > right_m:
        moving_right = apple - right_m
        count += moving_right
        left_m += moving_right
        right_m += moving_right

print(count)
