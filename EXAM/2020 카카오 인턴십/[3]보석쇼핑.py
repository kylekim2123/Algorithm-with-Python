def solution(gems):
    count = len(set(gems))
    gems_type = {}
    start, end = 0, 0
    answer = [1, len(gems)]

    while start <= end < len(gems):
        if len(gems_type) == count and all(gems_type.values()):
            gems_type[gems[start]] -= 1
            start += 1
            if answer[1]-answer[0] > end-start:
                answer[0], answer[1] = start, end
        else:
            gems_type.setdefault(gems[end], 0)
            gems_type[gems[end]] += 1
            end += 1

    return answer
        
gems = 	["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))