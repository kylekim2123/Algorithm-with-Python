def solution(numbers):
    answer = []
    for number in numbers:
        temp = number + 1
        while True:
            if len(format(number^temp, 'b').replace('0', '')) <= 2:
                answer.append(temp)
                break
            temp += 1
    return answer