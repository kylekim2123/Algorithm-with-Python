def drive(start, count, battery):
    global min_count
    if count >= min_count: # 이미 최소 횟수보다 많이 들렀으면 리턴
        return
    if start >= n-1: # 도착지에 도착했다면
        min_count = count # 최소 횟수 갱신
        return
    if battery >= m[start]: # 남은 배터리가 새로 충전할 배터리보다 많으면 리턴
        return
    for i in range(1, m[start]+1):
        drive(start+i, count+1, m[start]-i)


for t in range(1, int(input())+1):
    n, *m = map(int, input().split())
    min_count = n - 2 # 모든 충전소를 다 들르는 경우의 횟수
    drive(0, 0, 0)
    print('#%s %s' % (t, min_count-1))