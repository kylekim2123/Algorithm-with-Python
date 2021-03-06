# 11729. 하노이 탑 이동 순서 (실버2)

# 가장 밑의 원판을 제외한 n-1개의 원판을 일단 가운데로 옮기고
# 가장 밑의 원판을 맨 오른쪽에 옮긴다음
# n-1개의 원판을 맨 오른쪽에 옮긴다고 생각하며 재귀로 푼다.

def hanoi(number, start, middle, end):
    if number == 1:
        print(start, end) # 원판이 하나 남은 경우
        return
    hanoi(number-1, start, end, middle)
    print(start, end)
    hanoi(number-1, middle, start, end)

n = int(input())
print((2**n)-1) # 하노이 탑 최소 이동 횟수 공식
hanoi(n, 1, 2, 3)