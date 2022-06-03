# 72414. 광고 삽입


def get_seconds(time_string):
    hour, minute, second = time_string.split(":")
    hour, minute, second = int(hour), int(minute), int(second)
    return hour * 3600 + minute * 60 + second


def get_formatted_time(second):
    result = [str(second // 3600)]
    second %= 3600
    result.append(str(second // 60))
    second %= 60
    result.append(str(second))
    return ":".join(["0" * (2 - len(item)) + item for item in result])


def solution(play_time, adv_time, logs):
    play_time, adv_time = get_seconds(play_time), get_seconds(adv_time)
    viewers = [0] * (play_time + 1)  # 누적 시청자 수를 저장

    for index in range(len(logs)):
        start, end = logs[index].split("-")
        start, end = get_seconds(start), get_seconds(end)

        viewers[start] += 1  # 시청자 유입
        viewers[end] -= 1  # 시청자 이탈

    # 해당 시간대의 시청자 수 계산
    for time in range(1, len(viewers)):
        viewers[time] += viewers[time - 1]

    # 해당 시간대의 누적 시청자 수 계산
    for time in range(1, len(viewers)):
        viewers[time] += viewers[time - 1]

    start, end = 0, adv_time  # 광고 시작 시간, 종료 시간
    answer, max_views = '00:00:00', viewers[end]  # 최대 시청자 수 정보
    for start in range(1, play_time - adv_time + 1):
        end = start + adv_time

        # 광고 종료 시간은 시청자 이탈 시간이므로 그 직전의 누적 시청자 수를 사용
        # 누적 시청자 수에서 광고 시작 직전 누적 시청자 수를 빼면 총 시청자 수
        views = viewers[end - 1] - viewers[start - 1]

        if max_views < views:  # 최대 시청자 수 갱신
            answer = get_formatted_time(start)
            max_views = views

    return answer
