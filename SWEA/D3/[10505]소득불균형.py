# 10505. 소득 불균형

for t in range(1, int(input())+1):
    n = int(input())
    salary = list(map(int, input().split()))
    avg = sum(salary) / n
    result = sum(s <= avg for s in salary)
    print(f'#{t} {result}')