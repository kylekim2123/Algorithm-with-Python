def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if i == 1:
            answer -= 1
            continue
        divisor = 2
        for j in range(2, i//2+1):
            if not i % j:
                divisor += 1
        print(i, divisor)
        answer -= i if divisor % 2 else -i
    return answer
