# 1983. 조교의 성적 매기기
from math import ceil

for t in range(1, int(input()) + 1):
    nk = list(map(int, input().split()))
    n = nk[0]
    k = nk[1]
    total_score_list = []

    for i in range(n):
        scores = list(map(int, input().split()))
        total_score = (scores[0] * 0.35) + (scores[1] * 0.45) + (scores[2] * 0.2)
        total_score_list.append(total_score)
        if i == k - 1:
            k_score = total_score
    
    total_score_list.sort(reverse=True)
    k_index = total_score_list.index(k_score) + 1
    k_evaluation = ceil(k_index / (n / 10)) - 1
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    print(f'#{t} {grades[k_evaluation]}')
