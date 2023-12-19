def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged_arr = []
    l_idx, r_idx = 0, 0
    len_left, len_right = len(left), len(right)
    while l_idx < len_left and r_idx < len_right:
        if left[l_idx] < right[r_idx]:
            merged_arr.append(left[l_idx])
            l_idx += 1
        else:
            merged_arr.append(right[r_idx])
            r_idx += 1

    merged_arr.extend(left[l_idx:])
    merged_arr.extend(right[r_idx:])
    return merged_arr

a = [5, 1, 9, 6, 8, 4, 2, 3]
print(merge_sort(a))
