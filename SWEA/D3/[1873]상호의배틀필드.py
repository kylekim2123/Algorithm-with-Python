# 1873. 상호의 배틀필드

for t in range(1, int(input())+1):
    h, w = map(int, input().split())
    game_map = [list(input()) for _ in range(h)]
    n = int(input())
    user_control = input()

    for i in range(h):
        for j in range(w):
            if game_map[i][j] in ['^', 'v', '<', '>']:
                row = i
                col = j
    
    for control in user_control:
        if control == 'U':
            if  row > 0 and game_map[row-1][col] == '.':
                game_map[row][col] = '.'
                row -= 1
                game_map[row][col] = '^'
            else:
                game_map[row][col] = '^'
        elif control == 'D':
            if row < h-1 and game_map[row+1][col] == '.':
                game_map[row][col] = '.'
                row += 1
                game_map[row][col] = 'v'
            else:
                game_map[row][col] = 'v'
        elif control == 'L':
            if col > 0 and game_map[row][col-1] == '.':
                game_map[row][col] = '.'
                col -= 1
                game_map[row][col] = '<'
            else:
                game_map[row][col] = '<'
        elif control == 'R':
            if col < w-1 and game_map[row][col+1] == '.':
                game_map[row][col] = '.'
                col += 1
                game_map[row][col] = '>'
            else:
                game_map[row][col] = '>'
        elif control == 'S':
            if game_map[row][col] == '^':
                for i in range(row, -1, -1):
                    if game_map[i][col] == '*':
                        game_map[i][col] = '.'
                        break
                    elif game_map[i][col] == '#':
                        break
            elif game_map[row][col] == 'v':
                for i in range(row, h):
                    if game_map[i][col] == '*':
                        game_map[i][col] = '.'
                        break
                    elif game_map[i][col] == '#':
                        break
            elif game_map[row][col] == '<':
                for i in range(col, -1, -1):
                    if game_map[row][i] == '*':
                        game_map[row][i] = '.'
                        break
                    elif game_map[row][i] == '#':
                        break
            elif game_map[row][col] == '>':
                for i in range(col, w):
                    if game_map[row][i] == '*':
                        game_map[row][i] = '.'
                        break
                    elif game_map[row][i] == '#':
                        break
    
    print(f'#{t}', end=' ')
    for line in game_map:
        print(''.join(line))
                        