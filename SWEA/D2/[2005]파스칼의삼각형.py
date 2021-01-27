# 2005. 파스칼의 삼각형

for t in range(1, int(input()) + 1):
    n = int(input())
    pascal = [[0] * n for _ in range(n)]
    for i in range(len(pascal)):
        pascal[i][0] = 1
        for j in range(1, len(pascal[i])):
            pascal[i][j] = sum(pascal[i - 1][j-1:j+1])
    
    print(f'#{t}')
    for line in pascal:
        for number in line:
            if number != 0:
                print(number, end=' ')
        print()  
