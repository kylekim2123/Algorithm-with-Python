# sum 함수 자체 구현
def get_sum(args):
    total = 0
    for arg in args:
        total += arg
    return total


# 조건에 맞는 부분집합의 개수 구하기
def count_subset(whole_set, length, total):
    count = 0
    for i in range(1, 1 << SIZE):
        subset = []
        for j in range(SIZE):
            if i & (1 << j):
                subset.append(whole_set[j]) # 부분집합 만들기
        if len(subset) == length and get_sum(subset) == total:
            count += 1 # 해당 부분집합의 길이와 합이 n과 k와 같으면 count + 1
    return count


SIZE = 12
A = [i for i in range(1, SIZE+1)]
T = int(input())
for t in range(1, T+1):
    n, k = map(int, input().split())
    print('#%s %s' % (t, count_subset(A, n, k)))
