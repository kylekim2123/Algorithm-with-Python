def comb(n, r):
    if r <= 0:
        print(tr)
        return
    if n < r:
        return
    tr[r-1] = an[n-1]
    comb(n-1, r-1)
    comb(n-1, r)

an = [1, 2, 3, 4]
n = len(an)
r = 3
tr = [0] * r

comb(n, r)