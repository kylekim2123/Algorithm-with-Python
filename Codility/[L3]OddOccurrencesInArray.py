from collections import Counter

def solution(A):
    A = Counter(A)
    for a in A:
        if A[a] % 2:
            return a