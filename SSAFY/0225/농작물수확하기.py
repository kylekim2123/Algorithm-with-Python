for t in range(1, int(input())+1):
    n = int(input())
    total, start = 0, n//2 # 첫 줄 부터 한줄씩 탐색하므로, 시작점은 줄의 가운데 부분
    for i in range(n): # 총 n 줄에 대해
        line = list(map(int, input())) # 각 줄 입력 받고
        total += sum(line[start:n-start]) # 시작점~끝점 더하기
        start += 1 if i >= n//2 else -1 # 가운데 줄을 넘어가면 그때부터는 더하는 갯수가 하나씩 줄음
    print('#%s %s' % (t, total))
