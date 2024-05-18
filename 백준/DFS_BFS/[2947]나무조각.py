# 2947. 나무 조각 (실버5)

import sys
input = sys.stdin.readline

numbers = list(map(int, input().split()))
correct = [1, 2, 3, 4, 5]
while numbers != correct:
    for i in range(4):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            print(*numbers)
