# 2019 카카오 인턴십 2번 튜플

def solution(s):
    answer = []
    numbers = s.replace('{', '').rstrip('}}').split('},')
    numbers.sort(key=len)
    for number in numbers:
        unit = (set(number.split(',')) - set(answer)).pop()
        answer.append(unit)
    return list(map(int, answer))
