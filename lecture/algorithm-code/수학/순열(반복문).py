# 반복문을 이용한 순열은 뽑을 갯수만큼 반복문이 필요하다.
# 4, 5, 6 카드 세장 중, 세장을 뽑는 경우의 수 (순서 고려)

N = 3
card = [4, 5, 6]

for i in range(N):
    for j in range(N):
        if j != i:
            for k in range(N):
                if k != i and k != j:
                    print(card[i], card[j], card[k])