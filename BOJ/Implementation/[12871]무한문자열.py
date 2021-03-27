# 12871. 무한 문자열 (실버5)

from math import gcd

def is_same(s_string, l_string, s_len, l_len):
    lcm = (s_len*l_len) // gcd(s_len, l_len)
    temp1, temp2 = s_string, l_string
    for _ in range((lcm//s_len)-1):
        s_string += temp1
    for _ in range((lcm//l_len)-1):
        l_string += temp2
    if s_string == l_string:
        return 1
    return 0

s, t = input(), input()
len_s, len_t = len(s), len(t)
if len_s >= len_t:
    result = is_same(t, s, len_t, len_s)
else:
    result = is_same(s, t, len_s, len_t)
print(result)


# 간단 풀이 (최소공배수가 아니라 그냥 공배수를 이용)
# s, t = input(), input()
# temp1 = s * len(t)
# temp2 = t * len(s)
# if temp1 == temp2:
#     print(1)
# else:
#     print(0)