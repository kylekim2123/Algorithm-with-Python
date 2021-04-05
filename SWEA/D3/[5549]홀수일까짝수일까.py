# 5549. 홀수일까 짝수일까

result = []
for t in range(1, int(input())+1):
    if int(input()[-1]) % 2:
        result.append(f'#{t} Odd')
    else:
        result.append(f'#{t} Even')
print('\n'.join(result))