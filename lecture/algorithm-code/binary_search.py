# 이진 탐색
def binary_search(a, key):
    start, end = 0, len(a)-1
    while start <= end:
        middle = (start+end) // 2
        if a[middle] == key:
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False

a = [1, 2, 3, 4, 5] # 이진 탐색 시, 반드시 정렬 상태여야 한다.
print(binary_search(a, 5))
print(binary_search(a, 8))