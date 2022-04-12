# 11729. 하노이 탑 이동 순서 (실버2)


def hanoi(start, middle, end, number):
    if number == 1:
        print(start, end)
        return

    hanoi(start, end, middle, number - 1)  # 가장 밑의 원판을 제외한 n-1개의 원판을 일단 가운데로 옮기고
    print(start, end)  # 가장 밑의 원판을 맨 오른 쪽에 옮긴 다음
    hanoi(middle, start, end, number - 1)  # n-1개의 원판을 맨 오른 쪽에 옮긴 다고 생각 하며 재귀로 푼다.


n = int(input())
print((2 ** n) - 1)  # 하노이 탑 이동 횟수 공식
hanoi(1, 2, 3, n)
