# 딕셔너리와 카운팅을 이용한 문자열 숫자 정렬
def counting_sort_by_string(a):
    numbers = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    b = [0] * 10 # 카운팅 배열
    c = [''] * len(a) # 정렬된 배열
    for num in a:
        b[numbers[num]] += 1 # 문자열을 숫자로 변환하여 b에 해당 값 + 1
    for i in range(1, len(b)):
        b[i] += b[i-1]
    for i in range(len(a)-1, -1, -1):
        b_idx = numbers[a[i]] # 문자열을 숫자로 변환하여 b의 인덱스로 할당
        c[b[b_idx]-1] = a[i]
        b[b_idx] -= 1
    return c


for _ in range(1, int(input())+1):
    t, n = input().split()
    raw_arr = list(input().split())
    sorted_arr = counting_sort_by_string(raw_arr)
    print(t)
    print(' '.join(sorted_arr))