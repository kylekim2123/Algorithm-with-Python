# 16922. 로마 숫자 만들기

from itertools import combinations_with_replacement

cases = {sum(combi) for combi in combinations_with_replacement([1, 5, 10, 50], int(input()))}
print(len(cases))
