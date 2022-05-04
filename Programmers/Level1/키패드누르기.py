# 2020 카카오 인턴십 키패드 누르기 (Level 1)


def solution(numbers, hand):
    pad = [
        (3, 1),
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 0),
        (1, 1),
        (1, 2),
        (2, 0),
        (2, 1),
        (2, 2),
    ]

    answer = ""
    left, right = (3, 0), (3, 2)

    for n in numbers:
        if n in {1, 4, 7}:
            answer += "L"
            left = pad[n]
        elif n in {3, 6, 9}:
            answer += "R"
            right = pad[n]
        else:
            nx, ny = pad[n]
            left_dist = abs(nx - left[0]) + abs(ny - left[1])
            right_dist = abs(nx - right[0]) + abs(ny - right[1])

            if left_dist < right_dist:
                answer += "L"
                left = pad[n]
            elif left_dist > right_dist:
                answer += "R"
                right = pad[n]
            else:
                if hand == "left":
                    answer += "L"
                    left = pad[n]
                else:
                    answer += "R"
                    right = pad[n]

    return answer
