# 1221. S/W 문제해결 기본 5일차 - GNS

def change_str_to_int(string):
    strings = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    return strings.index(string)

for _ in range(1, int(input()) + 1):
    first_line = input().split()
    case = first_line[0]
    length = int(first_line[1])
    numbers = list(input().split())
    sorted_numbers = sorted(numbers, key=change_str_to_int)
    print(case)
    print(*sorted_numbers)