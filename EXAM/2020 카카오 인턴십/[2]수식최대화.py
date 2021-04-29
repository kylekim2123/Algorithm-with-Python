from itertools import permutations
OPERATOR = {
    '+': lambda x, y: x+y,
    '-': lambda x, y: x-y,
    '*': lambda x, y: x*y
}

def solution(expression):
    numbers, operators, word = [], [], []
    for digit in expression:
        if digit.isdecimal():
            word.append(digit)
            continue
        numbers.append(int(''.join(word)))
        numbers.append(digit)
        operators.append(digit)
        word = []
    numbers.append(int(''.join(word)))
    
    results = []
    operator_types = set(operators)
    print(list(permutations(operator_types, len(operator_types))))
    for priority in permutations(operator_types, len(operator_types)):
        temp = list(numbers)
        for op in priority:
            i = 1
            while i < len(temp) - 1:
                if temp[i] == op:
                    cal_num = OPERATOR[op](temp[i-1], temp[i+1])
                    for _ in range(3):
                        temp.pop(i-1)
                    temp.insert(i-1, cal_num)
                    continue
                i += 1
        results.append(temp[0])
    print(results)
    return max(abs(result) for result in results)

expression = "50*6-3*2"
print(solution(expression))