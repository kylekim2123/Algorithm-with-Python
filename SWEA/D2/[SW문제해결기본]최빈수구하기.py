# S/W 문제해결 기본: 1일차 - 최빈수 구하기

result = []
for _ in range(1, int(input()) + 1):
    case_number = input()
    scores = list(map(int, input().split()))
    max_count = 1
    max_score = 0
    for score in scores:
        count = scores.count(score)
        if count > max_count:
            max_count = count
            max_score = score
        elif count == max_count:
            if score > max_score:
                max_score = score
    result.append(f'#{case_number} {max_score}')

for i in result:
    print(i)