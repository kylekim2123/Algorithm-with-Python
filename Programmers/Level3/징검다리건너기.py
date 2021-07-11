# 2019 카카오 개발자 겨울 인턴십 : 징검다리 건너기

def solution(stones, k):
    answer = 200000000
    for i in range(len(stones)-k+1):
        k_stones = stones[i:i+k]
        answer = min(answer, max(k_stones))
    return answer
