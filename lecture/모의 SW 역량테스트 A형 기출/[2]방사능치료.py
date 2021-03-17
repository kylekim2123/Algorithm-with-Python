def get_virus_positions(a1, b1, a2, b2):
    if a1 > a2:
        if b1 > b2:
            return a2, b2, a1, b1
        return a2, b1, a1, b2
    if b2 > b1:
        return a1, b1, a2, b2
    return a1, b2, a2, b1

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    viruses = []
    for _ in range(n):
        viruses.append(get_virus_positions(*map(int, input().split())))
    virus_zip = list(zip(*viruses))
    s1, e1, s2, e2 = min(virus_zip[0]), min(virus_zip[1]), max(virus_zip[2]), max(virus_zip[3])

    k = max_width = max(s2-s1, e2-e1)
    start, end = 1, k
    while start < end:
        center = (start+end) // 2
        max_treat = 0
        starting_point = s1 + max_width - center + 1
        for i in range(s1, starting_point):
            tx1, tx2 = i, i+center
            for j in range(s1, starting_point):
                ty1, ty2 = j, j+center
                treat = 0
                for virus in viruses:
                    if tx1 <= virus[0] and virus[2] <= tx2 and ty1 <= virus[1] and virus[3] <= ty2:
                        treat += 1
                max_treat = max(max_treat, treat)
        if n - max_treat <= m:
            end = center
            k = center
        else:
            start = center + 1
    print('#%s %s' % (t, k))



