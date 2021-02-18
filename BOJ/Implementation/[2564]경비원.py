# 2564. 경비원 (실버1)

w, h = map(int, input().split())
n = int(input())
s_loc = [list(map(int, input().split())) for _ in range(n)]
d_dir, d_coo = map(int, input().split())

sum_dist = 0
for s_dir, s_coo in s_loc:
    if d_dir == s_dir:
        sum_dist += abs(d_coo-s_coo)
    elif d_dir == 1 or d_dir == 2:
        if s_dir != 3 and s_dir != 4:
            sum_dist += min(d_coo+s_coo, (w*2)-(d_coo+s_coo))+h
        else:
            sum_dist += d_coo if s_dir == 3 else w-d_coo
            sum_dist += s_coo if d_dir == 1 else h-s_coo
    else:
        if s_dir != 1 and s_dir != 2:
            sum_dist += min(d_coo+s_coo, (h*2)-(d_coo+s_coo))+w
        else:
            sum_dist += d_coo if s_dir == 1 else h-d_coo
            sum_dist += s_coo if d_dir == 3 else w-s_coo
print(sum_dist)