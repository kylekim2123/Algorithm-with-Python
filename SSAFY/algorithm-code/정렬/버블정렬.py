def bubble_sort(a):
    for i in range(len(a)-1, 0, -1): # 매 정렬 시 끝 위치가 하나씩 좁아짐
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
