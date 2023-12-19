# 선택 정렬
def selection_sort(a):
    for i in range(len(a)-1):
        min_index = i
        for j in range(i+1, len(a)):
            if a[min_index] > a[j]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]

a = [1, 5, 0, -2, 84, 30]
selection_sort(a)
print(a)