# 골드 5

import sys

input = sys.stdin.readline

PALINDROME = 0
PSEUDO_PALINDROME = 1
NORMAL_STRING = 2


def is_palindrome(start, end):
    while start < end:
        if word[start] != word[end]:
            return False

        start += 1
        end -= 1

    return True


def check(start, end):
    while start < end:
        if word[start] == word[end]:
            start += 1
            end -= 1

            continue

        if is_palindrome(start + 1, end) or is_palindrome(start, end - 1):
            return PSEUDO_PALINDROME

        return NORMAL_STRING

    return PALINDROME


for _ in range(int(input())):
    word = input().rstrip()
    print(check(0, len(word) - 1))
