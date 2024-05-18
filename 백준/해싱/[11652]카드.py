# 11652. 카드 (실버4)

import sys
from collections import Counter

input = sys.stdin.readline

number_counts = Counter(int(input()) for _ in range(int(input())))
max_count = max(number_counts.values())

print(sorted(x for x in number_counts if number_counts[x] == max_count)[0])
