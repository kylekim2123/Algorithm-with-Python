# 골드 1

import sys

input = sys.stdin.readline
SIZE = 30
MOD = 998_244_353


def get_total(line, target):
    count, total = 0, 0

    for bit in line:
        count += 1 if bit == target else -count
        total += count

    return total


def calculate_and(line):
    return get_total(line, 1)


def calculate_or(line):
    return whole_case - get_total(line, 0)


def calculate_xor(line):
    even_count, odd_count = 1, 0
    temp_bit = 0

    for bit in line:
        temp_bit ^= bit
        if temp_bit == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count * odd_count


n = int(input())
numbers = list(map(int, input().split()))
bits = [[] for _ in range(SIZE)]

for number in numbers:
    for bit in bits:
        bit.append(number % 2)
        number //= 2

whole_case = sum(range(1, n + 1))
total_and, total_or, total_xor = 0, 0, 0

for i, line in enumerate(bits):
    digit = (2 ** i) % MOD
    total_and += calculate_and(line) * digit
    total_or += calculate_or(line) * digit
    total_xor += calculate_xor(line) * digit

    total_and %= MOD
    total_or %= MOD
    total_xor %= MOD

print(total_and, total_or, total_xor)
