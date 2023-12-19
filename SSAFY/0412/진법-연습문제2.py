def hex_to_binary_four_digits(hex_number):
    hex_to_int_num = int(hex_number, 16) # 16진수 -> 10진수
    int_to_binary_num = format(hex_to_int_num, 'b') # 10진수 -> 2진수
    return int_to_binary_num.zfill(4) # 4자리로 맞춰줌(공백은 0으로 채운다)

for t in range(1, int(input())+1):
    hex_line = input()
    binary_line = ''
    for hex_num in hex_line:
        binary_line += hex_to_binary_four_digits(hex_num) # 16진수 -> 2진수
    
    result = []
    for i in range(0, len(binary_line), 7): # 7개씩 잘라서 변환
        binary_to_int_num = int(binary_line[i:i+7], 2) # 2진수 -> 10진수
        result.append(binary_to_int_num)
    print('#%s' % t, ', '.join(map(str, result)))