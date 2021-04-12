def binary_to_int(binary_number):
    unit = 2**(len(binary_number)-1) # 가장 높은 자릿수에 곱해줄 값
    int_num = 0 # 변환될 정수
    for binary_digit in binary_number: # 각 자릿수 마다
        int_num += binary_digit * unit # (자릿수 * 자릿수에 해당하는 값)을 정수에 더함
        unit //= 2 # 자릿수 하나씩 떨어뜨림
    return int_num

BIT = 7
for t in range(1, int(input())+1):
    binary_line = list(map(int, input())) # 0과 1로 이루어진 배열
    result = [binary_to_int(binary_line[i:i+BIT]) for i in range(0, len(binary_line), BIT)] # 7개씩 잘라서 10진수로 변환
    print('#%s' % t, ', '.join(map(str, result)))