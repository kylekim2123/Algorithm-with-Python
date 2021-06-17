def solution(A):
    MAX_INTERSECTIONS = 10**7
    circles = [(j-radius, j+radius) for j, radius in enumerate(A)]
    len_circles = len(circles)
    intersections = 0
    for j in range(len_circles):
        left_j, right_j = circles[j]
        for k in range(j+1, len_circles):
            left_k, right_k = circles[k]
            if (right_j < left_k) or (right_k < left_j):
                continue
            intersections += 1
    return intersections if intersections < MAX_INTERSECTIONS else -1
