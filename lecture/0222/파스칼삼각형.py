for t in range(1, int(input())+1):
    n = int(input())
    print('#%s' % t)
    print(1) # 맨 윗줄 1을 미리 출력
    for i in range(1, n):
        now_line = [1] # 매 줄마다 처음 등장하는 수 1
        for j in range(i-1): # i는 pre_line의 length와 같다. j+1을 보기 때문에 i-1까지 돌려야 인덱스 에러가 안난다.
            now_line.append(pre_line[j]+pre_line[j+1]) # 파스칼 삼각형은 pre_line의 두 요소를 합한 값이 now_line의 요소가 된다.
        now_line.append(1) # 매 줄마다 마지막에 등장하는 수 1
        pre_line = now_line # 현재 라인은 이제 이전 라인이 된다.
        print(*now_line)
