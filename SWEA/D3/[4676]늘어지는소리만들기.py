# 4676. 늘어지는 소리 만들기

for t in range(1, int(input())+1):
    word, h, locations = input(), int(input()), list(map(int, input().split()))
    numbers = [0] * (len(word)+1)
    for location in locations:
        numbers[location] += 1
    result = []
    for i in range(len(word)):
        result.append('-' * numbers[i])
        result.append(word[i])
    result.append('-' * numbers[-1])
    print(f'#{t} {"".join(result)}')
    