for t in range(1, 11):
    n, word = input().split()
    stack = []
    for unit in word: # 기존 비밀번호에서 한글자씩 가져온다
        if stack and stack[-1] == unit: # 스택이 비어있지 않고, 이미 스택의 최상단에 있는 문자와 같다면, 연속된 비밀번호이다.
            stack.pop() # 연속된 비밀번호는 제거
            continue
        stack.append(unit) # 연속되지 않았다면 스택에 삽입
    print('#%s %s' % (t, ''.join(stack))) # 연속되지 않은 것들은 최종 비밀번호
