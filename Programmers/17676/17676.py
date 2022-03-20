# 17676. [1차] 추석 트래픽


def make_pretty_time(time):
    """
    time string을 밀리초 기준의 정수로 변환하여 반환
    """
    hour, minute, second = time.split(":")
    s, ms = map(int, second.split("."))
    return int(hour) * 3600000 + int(minute) * 60000 + s * 1000 + ms


def solution(lines):
    answer = 0

    times = []  # 모든 처리시간의 시작 시간과 끝 시간을 저장할 리스트
    for num, line in enumerate(lines):
        date, end, period = line.split()  # 날짜, 처리시간의 종료 시간, 처리시간

        # 처리시간의 형태에 따라 정수로 변환하여 초와 밀리초를 기록
        period = period[:-1].split(".")
        if 1 < len(period):
            s, ms = int(period[0]), int(period[1] + "0" * (3 - len(period[1])))
        else:
            s, ms = int(period[0]), 0

        # 시작 시각과 끝 시각 기록
        times.append((make_pretty_time(end) - s * 1000 - ms + 1, num, "astart"))
        times.append((make_pretty_time(end), num, "end"))

    times.sort()

    num_set = set()  # 현재 포함되어있는 처리 번호를 저장할 세트
    for index, (time, num, status) in enumerate(times):
        # 현재 구간 = time ~ time + 1000 밀리초
        # 현재 구간에서 시작되거나 끝나는 처리 번호를 세트에 기록
        while index < len(times) and times[index][0] < time + 1000:
            next_time, next_num, next_status = times[index]
            if next_num not in num_set:
                num_set.add(next_num)
            index += 1

            answer = max(answer, len(num_set))  # 최댓값 갱신

            # 만약 처리시간이 끝났다면 다음 시간 구간에서 현재 처리 번호는 포함되지 않아야 하므로
            # 다음 for loop가 돌기 전 세트에서 현재 처리 번호를 제거
            if status == "end":
                num_set.remove(num)

        return answer
