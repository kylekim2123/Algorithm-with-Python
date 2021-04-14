def combi(i, j, n, r):
    if i == r:
        print(c)
        return
    for k in range(j, n-r+i+1):
        c[i] = A[k]
        combi(i+1, k+1, n, r)

A = [1, 2, 3, 4, 5, 6]
n = len(A)
r = 3
c = [0] * r
combi(0, 0, n, r)
