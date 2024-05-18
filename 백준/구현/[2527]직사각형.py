# 2527. 직사각형 (실버1)

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    touch = [p1 == x2, p2 == x1, q1 == y2, q2 == y1]
    t_count = touch.count(True)
    if t_count >= 1:
        if t_count >= 2:
            print('c')
        else:
            print('b')
    elif p1 < x2 or p2 < x1 or q1 < y2 or q2 < y1:
        print('d')
    else:
        print('a')