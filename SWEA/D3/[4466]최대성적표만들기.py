# 4466. 최대 성적표 만들기

for  t in range(1, int(input())+1):
    n, k = map(int, input().split())
    scores = sorted(list(map(int, input().split())), reverse=True)
    print(f'#{t} {sum(scores[:k])}')