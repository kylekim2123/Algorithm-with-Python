from collections import deque

def solution(s):
    brackets = deque(s)
    length = len(brackets)
    answer = 0
    opens = {'[', '(', '{'}
    matches = {']': '[', ')': '(', '}': '{'}
    for _ in range(length):
        stack = []
        for bracket in brackets:
            if bracket in opens:
                stack.append(bracket)
                continue
            if not stack or stack.pop() != matches[bracket]:
                break
        else:
            if not stack:
                answer += 1
        brackets.append(brackets.popleft())
    return answer

print(solution('{{'))