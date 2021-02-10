# 1343. 폴리오미노 (실버4)

X = input().split('.')
X_length = len(X)
result = []
for i in range(X_length):
    length = len(X[i])
    if length % 2:
        print(-1)
        break
    result.append('AAAA' * (length//4))
    result.append('BB' * ((length%4)//2))
    if i < X_length-1 and X_length > 1:
        result.append('.')
else:
    print(''.join(result))