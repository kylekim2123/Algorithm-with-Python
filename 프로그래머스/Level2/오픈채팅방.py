# 2019 KAKAO BLIND RECRUITMENT 오픈 채팅방 (Level 2)


def solution(record):
    printing = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    uids, actions = [], []
    id_name = {}

    for r in record:
        inputs = r.split()

        if inputs[0] != "Leave":
            id_name[inputs[1]] = inputs[2]

        if inputs[0] != "Change":
            uids.append(inputs[1])
            actions.append(printing[inputs[0]])

    answer = [id_name[uids[i]] + actions[i] for i in range(len(uids))]

    return answer
