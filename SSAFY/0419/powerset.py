def powerset(depth, total):
    if total > m: # 합이 목표값(m)보다 커지면 가지치기
        return
    if total == m: # 합이 목표값(m)과 일치하면, count++
        global count
        count += 1
        return
    if depth < n: # depth가 n보다 작은 경우만, 다음 depth로 넘어감 (depth가 n인 경우 더이상 진행 X)
        powerset(depth+1, total+arr[depth]) # 부분집합으로 포함하여 진행
        powerset(depth+1, total) # 부분집합으로 포함하지 않고 진행


for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0
    powerset(0, 0)
    print('#%s %s' % (t, count))