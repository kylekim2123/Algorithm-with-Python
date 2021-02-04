# 1032. 명령 프롬프트

n = int(input())
texts = []
for _ in range(n):
    texts.append(input())

columns = list(zip(*texts))
result = ''
for column in columns:
    if column.count(column[0]) < n:
        result += '?'
    else:
        result += column[0]

print(result)
