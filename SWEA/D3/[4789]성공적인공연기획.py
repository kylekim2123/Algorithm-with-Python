# 4789. 성공적인 공연 기획

for t in range(1, int(input())+1):
    people = list(map(int, input()))
    total, employment = people[0], 0
    if not total:
        total += 1
        employment += 1
    for i in range(1, len(people)):
        if i > total:
            total += 1
            employment += 1
        total += people[i]
    print(f'#{t} {employment}')