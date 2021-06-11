seconds = {0: [1, 1], 1: [3, 2], 2: [5, 4], 3: [7, 6]}

for t in range(1, int(input())+1):
    question, answer = input(), input()
    total = 0
    for i in range(4):
        question_num, answer_num = ord(question[i]), ord(answer[i])
        clock = (90-answer_num)+(question_num-64) if question_num < answer_num else question_num-answer_num
        counter_clock = (90-question_num)+(answer_num-64) if question_num > answer_num else answer_num-question_num

        clock *= seconds[i][0]
        counter_clock *= seconds[i][1]

        total += min(clock, counter_clock)
    print(f'#{t} {total}')