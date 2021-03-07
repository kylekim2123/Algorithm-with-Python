# 2023. 신기한 소수 (골드5)

def is_prime(number):
    for i in range(3, int(number**(0.5))+1, 2):
        if number % i == 0:
            return False
    return True

def dfs(s):
    if not is_prime(int(s)):
        return
    if len(s) == n:
        result.append(s)
        return
    for end in ends:
        dfs(s+end)

n = int(input())
starts = ['2', '3', '5', '7']
ends = ['1', '3', '7', '9']
result = []
for start in starts:
    dfs(start)
print('\n'.join(result))