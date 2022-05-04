# 2021 KAKAO BLIND RECRUITMENT 신규 아이디 추천 (Level 1)


def solution(new_id):
    answer = ""
    allowed_chars = {"-", "_", "."}

    # 1, 2단계
    for char in new_id.lower():
        if char.isalnum() or char in allowed_chars:
            answer += char

    # 3단계
    while ".." in answer:
        answer = answer.replace("..", ".")

    # 4단계
    answer = answer.strip(".")

    # 5단계
    if not answer:
        answer = "a"

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15].rstrip(".")

    # 7단계
    while len(answer) <= 2:
        answer += answer[-1]

    return answer
