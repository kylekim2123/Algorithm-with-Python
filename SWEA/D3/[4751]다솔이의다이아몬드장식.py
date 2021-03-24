# 4751. 다솔이의 다이아몬드 장식

for t in range(1, int(input())+1):
    word = input()
    width = (len(word)*4)+1
    decoration = [['.'] * width for _ in range(5)]
    for i in range(2, width, 4):
        decoration[0][i] = '#'
        decoration[4][i] = '#'
    for i in range(1, width, 2):
        decoration[1][i] = '#'
        decoration[3][i] = '#'
    count, j = 1, 0
    for i in range(0, width, 2):
        if count % 2:
            decoration[2][i] = '#'
        else:
            decoration[2][i] = word[j]
            j += 1
        count += 1
    for line in decoration:
        print(''.join(line))