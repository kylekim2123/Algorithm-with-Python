def solution(N, A):
    result = [0] * N
    last_max_x = 0
    max_x = 0
    for x in A:
        if x > N:
            last_max_x = max_x
            continue
        if result[x-1] < last_max_x:
            result[x-1] = last_max_x + 1
        else:
            result[x-1] += 1
        max_x = max(max_x, result[x-1])
    for i in range(N):
        result[i] = max(result[i], last_max_x)
    return result
        

print(solution(5, [1, 4, 1, 4, 1, 4, 1, 6]))