# 1. 네오와 프로도의 숫자놀이

NUMBER = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def solution(s):
    if not s.isdecimal():
        for number in NUMBER:
            s = s.replace(number, NUMBER[number])
    return int(s)