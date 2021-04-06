def count_subtree(node):
    global count
    count += 1 # 서브트리 노드 개수 + 1
    if left[node]:
        count_subtree(left[node]) # 왼쪽 노드값 있으면 갯수 세러 감
    if right[node]:
        count_subtree(right[node]) # 오른쪽 노드값 있으면 갯수 세러 감

for t in range(1, int(input())+1):
    e, n = map(int, input().split())
    pairs = list(map(int, input().split()))
    left, right = [0]*(e+2), [0]*(e+2) # e는 간선의 수이므로 +2 를 했음(노드의 수였다면 +1)
    for i in range(0, e*2-1, 2):
        if left[pairs[i]]:
            right[pairs[i]] = pairs[i+1] # 왼쪽 노드값이 있으면 오른쪽에 추가
        else:
            left[pairs[i]] = pairs[i+1] # 왼쪽 노드값이 없으면 왼쪽에 추가
    count = 0
    count_subtree(n)
    print('#%s %s' % (t, count))
    