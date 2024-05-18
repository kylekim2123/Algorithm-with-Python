def solution(gems):
    count = len(set(gems))
    length = len(gems)
    gems_type = {gems[0]: 1}
    start, end = 0, 0
    answer = [0, length-1]

    while end < length:
        if len(gems_type) == count:
            if answer[1]-answer[0] > end-start:
                answer[0], answer[1] = start, end
            if gems_type[gems[start]] == 1:
                del gems_type[gems[start]]
            else:
                gems_type[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end >= length:
                break
            gems_type.setdefault(gems[end], 0)
            gems_type[gems[end]] += 1

    answer[0] += 1
    answer[1] += 1
    return answer
        
gems = ['DIA', 'EM', 'EM', 'RUB', 'DIA']
print(solution(gems))