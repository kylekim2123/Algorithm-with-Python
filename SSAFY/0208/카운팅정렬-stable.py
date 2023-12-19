def counting_sort(raw_arr, max_v):
    count_arr = [0] * (max_v + 1) # 카운트 배열
    sorted_arr = [0] * len(raw_arr) # 정렬할 배열

    # 카운트 배열 만들기
    for i in range(len(raw_arr)):
        first_num = int(raw_arr[i][0])
        count_arr[first_num] += 1

    # 카운트 배열 누적하기
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    # 정렬하기
    for i in range(len(raw_arr)-1, -1, -1): # stable sorting 을 위해 인덱스를 거꾸로 탐색
        count_index = int(raw_arr[i][0])
        sorted_arr[count_arr[count_index]-1] = raw_arr[i]
        count_arr[count_index] -= 1

    return sorted_arr


T = int(input())
for t in range(1, T+1):
    n = int(input())
    raw_list = list(input().split())

    max_value = 0
    for i in range(len(raw_list)):
        now_value = int(raw_list[i][0])
        if now_value > max_value:
            max_value = now_value

    sorted_list = counting_sort(raw_list, max_value)
    print('#%s' % t, end=' ')
    print(*sorted_list)