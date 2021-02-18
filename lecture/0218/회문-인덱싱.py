# 풀이1. 인덱싱을 이용해 회문 찾기

# 회문 찾기
def find_palindrome(words, n, m):
    for word in words:
        for start in range(0, n-m+1): # 완전 탐색
            i, j = start, start+m-1
            while i < j:
                if word[i] != word[j]:
                    break # 글자가 하나라도 다르면 회문이 아님
                i += 1
                j -= 1
            else:
                return ''.join(word[start:start+m])
    return '' # 회문이 없으면 빈 문자열 반환

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
        continue # 회문이 있다면 세로로 찾지 않고 넘긴다
    get_zip(words, n)
    print('#%s %s' % (t, find_palindrome(words, n, m))) # 세로 기준으로 회문 찾기
