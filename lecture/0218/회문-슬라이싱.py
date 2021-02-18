# 풀이2. 슬라이싱을 이용해 회문 찾기

# 회문 찾기
def find_palindrome(words, n, m):
    for word in words:
        for i in range(0, n-m+1):
            if word[i:i+m] == word[i+m-1:i:-1]+[word[i]]: # 슬라이싱으로 뒤집고 비교
                return ''.join(word[i:i+m])
    return ''

# zip 함수 구현
def get_zip(words, n):
    for i in range(n):
        for j in range(n):
            if i < j:
                words[i][j], words[j][i] = words[j][i], words[i][j]

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    words = [list(input()) for _ in range(n)]
    palindrome = find_palindrome(words, n, m) # 가로 기준으로 회문 찾기
    if palindrome:
        print('#%s %s' % (t, palindrome))
        continue
    get_zip(words, n)
    print('#%s %s' % (t, find_palindrome(words, n, m))) # 세로 기준으로 회문 찾기
