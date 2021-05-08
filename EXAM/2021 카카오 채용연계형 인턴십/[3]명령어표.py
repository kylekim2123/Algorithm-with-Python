# 3. 앙몬드의 명령어 기반 표

def solution(n, k, cmd):
    table = list(range(n))
    stack = []
    for key in cmd:
        ops = key.split()
        if ops[0] == 'U':
            k -= int(ops[1])
        elif ops[0] == 'D':
            k += int(ops[1])
        elif ops[0] == 'C':
            stack.append((k, table.pop(k)))
            if k >= len(table):
                k -= 1
        elif ops[0] == 'Z':
            idx, back = stack.pop()
            table.insert(idx, back)
            if idx <= k:
                k += 1

    answer = ['O'] * n
    for _, number in stack:
        answer[number] = 'X'
    return ''.join(answer)

n, k = 8, 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(n, k, cmd))