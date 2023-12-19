# 슬라이싱을 이용한 회문2 풀이 -> 오래 걸림
SIZE = 100
def len_palindrome(word, max_count):
    for length in range(SIZE, 1, -1): # 길이 100부터 탐색하여 불필요한 반복 제거
        if length <= max_count:
            return 0 # 이미 구해진 최대 길이보다 짧으면 더 볼 것도 없음
        for start in range(0, SIZE - length + 1):
            temp = word[start:start + length]
            if temp == temp[::-1]: # 회문 확인
                return length

for _ in range(1, 11):
    t = int(input())
    words = [list(input()) for _ in range(SIZE)]
    max_count = 1
    for word in words:
        max_count = max(max_count, len_palindrome(word, max_count))

    words = list(zip(*words)) # 세로로 보기
    for word in words:
        max_count = max(max_count, len_palindrome(word, max_count))

    print('#%s %s' % (t, max_count))