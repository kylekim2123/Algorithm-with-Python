# 1952. 수영장

def dfs(start, total):
    if start > 12:
        global min_total
        min_total = min(min_total, total)
        return
    dfs(start+1, total+(costs[0]*plans[start-1]))
    dfs(start+1, total+costs[1])
    dfs(start+3, total+costs[2])

for t in range(1, int(input())+1):
    costs, plans = list(map(int, input().split())), list(map(int, input().split()))
    min_total = costs[3]
    dfs(1, 0)
    print(f'#{t} {min_total}')