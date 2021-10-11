# 19583. 싸이버개강총회


def attendance(time_record, nickname):
    global present_set, attendance_cnt

    hour, minute = time_record[:2], time_record[3:]

    # 개강총회 시작 이전
    if hour < start_h or (hour == start_h and minute <= start_min):
        present_set.add(nickname)

    # 개강총회 시작 이후 ~ 스트리밍 종료 이전
    elif end_h < hour or (hour == end_h and end_min <= minute):
        if hour < quit_h or (hour == quit_h and minute <= quit_min):
            if nickname in present_set:  # 출석을 했던 사람의 경우
                present_set.discard(nickname)  # 중복된 출석 확인 제외
                attendance_cnt += 1


S, E, Q = input().split()

# 시작한 시, 분 / 끝낸 시, 분 / 스트리밍 종료 시, 분
start_h, start_min = S[:2], S[3:]
end_h, end_min = E[:2], E[3:]
quit_h, quit_min = Q[:2], Q[3:]

present_set = set()  # 스트리밍 시작 전 출석 명단
attendance_cnt = 0  # 출석이 확인된 인원 수
while True:
    try:
        record = list(input().split())
    except EOFError:
        break
    attendance(record[0], record[1])

print(attendance_cnt)