SIZE = 12
def dfs(start, count, total):
    if count == n and total == k:
        global subset
        subset += 1 # n개의 원소이고 합이 k이면 부분집합 개수 + 1
        return
    for i in range(start+1, SIZE+1): # 자신보다 다음 수부터 부분집합 추출
        dfs(i, count+1, total+i) # (자신, 개수+1, 합계+자신) 으로 갱신하여 재귀

for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    subset = 0
    dfs(0, 0, 0)
    print('#%s %s' % (t, subset))