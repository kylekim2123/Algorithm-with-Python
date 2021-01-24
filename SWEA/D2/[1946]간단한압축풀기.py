# 1946. 간단한 압축 풀기

results = list()
for t in range(1, int(input()) + 1):
    temp = ''
    for _ in range(int(input())):
        zip_info = list(input().split())
        temp += (zip_info[0] * int(zip_info[1]))

    result = ''
    start_index = 0
    for i in range(1, len(temp) + 1):
        if i == len(temp):
            result += temp[start_index:i]
            break
        if i % 10 == 0:
            result += (temp[start_index:i] + '\n')
            start_index = i
    results.append(result)

count = 1
for result in results:
    print(f'#{count}')
    print(result)
    count += 1