# 92342. 양궁대회


from collections import deque


def solution(n, info):
    answer = [[-1]]
    score_difference = 0

    # (맞춰야 하는 점수의 인덱스, 남은 화살 수, 총 점수, 기록)를 덱에 기록
    dq = deque([(0, n, 0, [0] * 11)])
    while dq:
        score, left_arrow, total, record = dq.popleft()

        if score == 11 or left_arrow == 0:  # 경기가 종료되는 경우
            # 남은 화살이 있다면 가장 낮은 점수를 더 많이 맞히도록 기록 변경
            if left_arrow:  
                record[-1] += left_arrow

            lion_total, peach_total = 0, 0  # 라이언의 점수, 어피치의 점수
            for score, (lion, peach) in enumerate(zip(record, info)):
                if lion < peach and peach:
                    peach_total += 10 - score
                elif peach < lion and lion:
                    lion_total += 10 - score

            if peach_total < lion_total:  # 라이언이 승리한 경우
                # 라이언이 최고 점수를 갱신하며 승리한 경우
                if score_difference < lion_total - peach_total:
                    score_difference = lion_total - peach_total
                    answer = [record]

                # 라이언이 최고 점수를 유지하며 승리한 경우
                elif score_difference == lion_total - peach_total:
                    answer.append(record)
            continue

        # 맞춰야하는 점수를 득점하는 경우
        if info[score] < left_arrow:
            new_record = record[:]
            new_record[score] = info[score] + 1
            dq.append((score + 1, left_arrow - info[score] - 1, total + 10 - score, new_record))

        # 맞춰야 하는 점수를 득점하지 않는 경우
        dq.append((score + 1, left_arrow, total, record))

    if 1 < len(answer):
        # 최고점수부터 득점을 했기 때문에 마지막 원소 == 가장 낮은 점수를 더 많이 맞힌 경우
        return answer[-1]
    else:
        return answer[0]
