# pop()을 사용하여 실행 시간이 긴 풀이
for t in range(1, int(input())+1):
    line = input()
    pieces = [] # 쇠막대기
    count = 0
    for bracket in line:
        if bracket == '(':
            pieces.append(0) # 여는 괄호일 때는 쇠막대기 추가
            continue
        if pieces[-1] == 0: # 레이저라면
            pieces.pop()
            for i in range(len(pieces)):
                pieces[i] += 1 # 레이저가 등장하면 쇠막대기에 +1 씩 더함
            continue
        count += pieces.pop()+1 # 레이저가 아니라면, +1을 더해서 count에 합함. 1번 자르면 2개의 토막이 생기기 때문
    print('#%s %s' % (t, count))