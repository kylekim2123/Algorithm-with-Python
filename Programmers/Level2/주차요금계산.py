# 2022 KAKAO BLIND RECRUITMENT 주차 요금 계산 (Level 2)

from datetime import datetime


# 주차 시간(out - in)을 분 단위로 계산
def get_minutes(i, o):
    in_time = datetime.strptime(i, "%H:%M")
    out_time = datetime.strptime(o, "%H:%M")

    return (out_time - in_time).total_seconds() / 60


def solution(fees, records):
    s_time, s_fee, u_time, u_fee = fees
    car = {}  # {차량번호: [누적시간, in, out]}
    cost = []

    for record in records:
        t, num, status = record.split()
        if num in car:
            if status == "IN":
                car[num].append(t)
            else:
                car[num][0] += get_minutes(car[num].pop(), t)
        else:
            car[num] = [0, t]

    for num in car:
        if len(car[num]) > 1:  # 출차가 없는 경우
            car[num][0] += get_minutes(car[num].pop(), "23:59")

        fee = s_fee  # 기본 요금
        remains = car[num][0] - s_time

        # 단위 요금 추가
        if remains > 0:
            i, mod = divmod(remains, u_time)
            fee += i * u_fee
            if mod > 0:
                fee += u_fee

        cost.append((int(num), int(fee)))

    # 차량번호 순으로 정렬 후 요금만 추출
    answer = [fee for _, fee in sorted(cost, key=lambda x: x[0])]

    return answer
