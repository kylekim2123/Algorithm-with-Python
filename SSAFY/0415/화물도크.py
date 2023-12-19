for t in range(1, int(input())+1):
    n = int(input())
    times = [list(map(int, input().split())) for _ in range(n)]
    times.sort(key=lambda x: x[1]) # 종료 시간을 기준으로 정렬하면 greedy 하게 풀 수 있다.
    max_truck, previous_end = 0, 0 # 가능한 최대 화물차 수, 바로 이전 작업의 종료시간
    for s, e in times: # 시작, 종료 시간
        if s >= previous_end: # 시작시간이 바로 이전 작업의 종료시간 이상이라면
            max_truck += 1 # 화물차는 작업이 가능하다
            previous_end = e # 그리고 해당 작업의 종료시간으로, 이전 작업 종료시간을 갱신
    print('#%s %s' % (t, max_truck))