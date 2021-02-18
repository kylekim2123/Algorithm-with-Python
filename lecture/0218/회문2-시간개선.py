# 인덱스를 이용해서 회문을 검사할 때 한글자씩 했더니 실행시간이 매우 줄었다.
SIZE = 100
def len_palindrome(word, max_count):
    for length in range(SIZE, 1, -1): # 길이 100부터 탐색하여 불필요한 반복 제거
        if length <= max_count:
            return 0 # 이미 구해진 최대 길이보다 짧으면 더 볼 것도 없음
        for start in range(0, SIZE - length + 1):
            i, j = start, start+length-1 # 문자열의 양끝부터 한글자씩 회문 검사
            while i < j:
                if word[i] != word[j]:
                    break  # 글자가 하나라도 다르면 회문이 아님
                i += 1
                j -= 1
            else:
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