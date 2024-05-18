# 3. 앙몬드의 명령어 기반 표

def solution(n, k, cmd):
    answer = ['O'] * n
    end = n - 1
    stack = []

    for key in cmd:
        ops = key.split()
        if ops[0] == 'U':
            i = 1
            ops = int(ops[i])
            while i <= ops:
                k -= 1
                if answer[k] == 'O':
                    i += 1
        elif ops[0] == 'D':
            i = 1
            ops = int(ops[i])
            while i <= ops:
                k += 1
                if answer[k] == 'O':
                    i += 1
        elif ops[0] == 'C':
            answer[k] = 'X'
            stack.append(k)
            if k >= end:
                for i in range(end-1, -1, -1):
                    if answer[i] == 'O':
                        end = i
                        break
                k = end
            else:
                for i in range(k+1, n):
                    if answer[i] == 'O':
                        k = i
                        break
        elif ops[0] == 'Z':
            back = stack.pop()
            answer[back] = 'O'
            if end < back:
                end = back

    return ''.join(answer)

n, k = 8, 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C", "U 2", "C", "D 1", "C", "U 1", "C", "C"]
print(solution(n, k, cmd))