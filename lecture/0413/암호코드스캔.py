# 각 숫자는 0과 1의 비율이 있는데, 이 중 세자리만 알아도 구별이 된다.
# 따라서 한 줄씩 읽을 때, 세자리의 비율을 구해서 각 코드가 어떤 숫자를 뜻하는지 찾는다.
NUMBERS = {
    '211': 0,
    '221': 1,
    '122': 2,
    '411': 3,
    '132': 4,
    '231': 5,
    '114': 6,
    '312': 7,
    '213': 8,
    '112': 9
}


# 16진수 -> 2진수 (4자리)
def hex_to_bin(hex_num):
    if hex_num == '0':
        return '0000'
    return format(int(hex_num, 16), 'b').zfill(4)


# 16진수로 이루어진 한 줄을 2진수 한 줄로 변환하는 함수
def change_to_bin_code(hex_code):
    if not hex_code:
        return '' # rstrip이 한 번 되어서 들어오므로, hex_code가 빈 값이라면 빈 문자열을 그대로 반환
    binary_code = []
    for hex_digit in hex_code:
        binary_code.append(hex_to_bin(hex_digit)) # 각 16진수 숫자를 2진수(4자리)로 바꾸어 2진수짜리 한 줄을 만듦
    return ''.join(binary_code).rstrip('0')


# 검증 코드가 올바른지 판단하고, 그에 따른 결과값을 반환하는 함수
def validate_and_calculate(code):
    check = ((code[0]+code[2]+code[4]+code[6]) * 3) + (code[1]+code[3]+code[5]) + code[7]
    return 0 if check % 10 else sum(code)


# 세 자리의 비율을 찾는 함수
def find_ratios(binary_code, i):
    second, third, fourth = 0, 0, 0 # 암호숫자 0~9는 각각 "first : second : third : fourth" 의 0과 1의 비율을 가진다. first는 취급하지 않는다.
    while binary_code[i] == '1':
        fourth += 1 # 뒤에서 부터 읽기 때문에, fourth 비율을 먼저 찾는다. 1이 몇개 있는지?
        i -= 1
    while binary_code[i] == '0':
        third += 1 # 1 다음에는 0이 오므로, third 비율은 0의 갯수로 찾는다.
        i -= 1
    while binary_code[i] == '1':
        second += 1 # third 다음에는 second이고, 1의 갯수로 비율을 찾는다.
        i -= 1
    while i >= 0 and binary_code[i] == '0':
        i -= 1 # 원래는 first의 비율을 찾아야 하지만, 여기서는 취급하지 않으므로, first 부분의 0은 skip한다.
    min_ratio = min(second, third, fourth)
    return i, [second//min_ratio, third//min_ratio, fourth//min_ratio] # 인덱스 i와 함께, 


def sum_code_number(code_arr):
    total = 0
    checked = set() # 이미 넣은 코드 중복 방지
    for binary_code in code_arr: # 한 줄씩 꺼낸다
        if binary_code:
            i = len(binary_code) - 1 # 뒤에서 부터 읽을 것이므로, 맨 뒤 인덱스 초기화
            code = [] # 암호코드 하나가 담길 곳
            while i >= 0:
                i, ratios = find_ratios(binary_code, i) # 세 자리의 비율을 찾는다
                code_key = ''.join(map(str, ratios))
                code.append(NUMBERS[code_key]) # 비율에 따른 해독 값을 암호코드 배열에 넣는다
                if len(code) == 8: # 해독 값을 다 찾으면
                    checked_code = ''.join(map(str, code))
                    if checked_code not in checked: # 중복인지 확인
                        checked.add(checked_code)
                        total += validate_and_calculate(code[::-1]) # 검증해서 정상이면 그 합을 더한다
                    code = []
    return total


for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    code_arr = [change_to_bin_code(input()[:m].rstrip('0')) for _ in range(n)]
    print('#%s %s' % (t, sum_code_number(code_arr)))
