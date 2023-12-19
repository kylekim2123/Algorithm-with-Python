# depth를 이용한 실행 시간 개선 풀이
for t in range(1, int(input())+1):
    line = input().replace('()', 'L') # 레이저 부분 문자열을 변경하면 탐색이 쉬워짐
    count, depth = 0, 0 # 결과값과 괄호깊이 선언
    for bracket in line:
        if bracket == '(':
            depth += 1 # 열린 괄호면, 깊이 + 1
        elif bracket == ')':
            count += 1 # 쇠막대기 하나가 끝날 때마다, 1을 더해서 보정해야함. 1번 자르면 2개가 되는 방식이기 때문
            depth -= 1 # 닫힌 괄호면 깊이 - 1
        else:
            count += depth # 레이저라면 깊이만큼 더한다. 깊이는 현재 레이저에 걸쳐있는 막대기의 개수와 같다.
    print('#%s %s' % (t, count))
