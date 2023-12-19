def counting_sort(a, k):
    # a 리스트: raw data, k : a 리스트 내의 최대값
    b = [0] * (k + 1) # 카운트 배열
    c = [0] * len(a) # 정렬할 배열

    # 카운트 배열 만들기
    for num in a:
        b[num] += 1

    # 카운트 배열 누적하기
    for i in range(1, len(b)):
        b[i] += b[i-1]

    # 정렬하기
    for i in range(len(a)-1, -1, -1): # stable sorting 을 위해 인덱스를 거꾸로 탐색
        c[b[a[i]]-1] = a[i]
        b[a[i]] -= 1

    return c

a = [5, 2, 0, 56, 84, 100, 3]
c = counting_sort(a, max(a))
print(c)