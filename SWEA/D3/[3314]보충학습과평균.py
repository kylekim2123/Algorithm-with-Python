# 3314. 보충학습과 평균

for t in range(1, int(input())+1):
    scores = list(map(lambda x: max(40, int(x)), input().split()))
    print(f'#{t} {sum(scores)//5}')
    