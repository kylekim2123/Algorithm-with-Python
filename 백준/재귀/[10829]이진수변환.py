# 10829. 이진수 변환 (브론즈1)

def binary(number):
    if number == 1:
        bi_num.append(1)
        return
    bi_num.append(number%2)
    binary(number//2)

n = int(input())
bi_num = []
binary(n)
print(''.join(map(str, bi_num[::-1])))