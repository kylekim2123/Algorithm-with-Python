def counting_sort_by_string(a):
    numbers = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    b = [0] * 10
    c = [''] * len(a)
    for num in a:
        b[numbers[num]] += 1
    for i in range(1, len(b)):
        b[i] += b[i-1]
    for i in range(len(a)-1, -1, -1):
        b_idx = numbers[a[i]]
        c[b[b_idx]-1] = a[i]
        b[b_idx] -= 1
    return c


for _ in range(1, int(input())+1):
    t, n = input().split()
    raw_arr = list(input().split())
    sorted_arr = counting_sort_by_string(raw_arr)
    print(t)
    print(' '.join(sorted_arr))