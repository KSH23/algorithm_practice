# 17678. [1차] 셔틀버스


def convert_to_minutes(time_string):
    hour, minute = time_string.split(":")
    return int(hour) * 60 + int(minute)


def solution(n, t, m, timetable):
    # 시간을 분으로 환산한 뒤 오름차순 정렬
    for index, time in enumerate(timetable):
        timetable[index] = convert_to_minutes(time)
    timetable.sort()

    index = 0  # 현재재 색할 timetable의 index
    now = convert_to_minutes("09:00")  # 현재 시간

    # 콘은 무조건 막차를 타야하기 때문에 막차 이전의 셔틀에 탈 수 있는 크루 제외
    for bus in range(n - 1):
        for _ in range(m):
            if index < len(timetable) and timetable[index] <= now:
                index += 1
        now += t

    # 막차에서 콘의 자리를 제외 해놓고, 탈 수 있는 크루 제외
    for cnt in range(m - 1):
        if index < len(timetable) and timetable[index] <= now:
            index += 1
        else:
            break
    
    # 남은 한 자리에 탈 수 있는 크루가 있다면 그 크루보다 먼저 도착
    if index < len(timetable) and timetable[index] <= now:
        answer = timetable[index] - 1
    
    # 남은 한 자리에 탈 수 있는 크루가 없다면 셔틀 도착 시간에 도착
    else:
        answer = now
    
    # 시간을 "hh:mm" 형태로 변환해 반환
    hour = str(answer // 60) if 10 <= answer // 60 else f"0{answer // 60}"
    minute = str(answer % 60) if 10 <= answer % 60 else f"0{answer % 60}"
    return hour + ":" + minute
