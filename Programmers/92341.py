# 92341. 주차 요금 계산


def make_pretty_time(time):
    """
    시간의 문자열을 받아 분 단위로 변환하여 반환하는 함수
    """
    hour, minute = time.split(":")
    return 60 * int(hour) + int(minute)


def solution(fees, records):
    answer = []

    in_dict = dict()  # 입차한 차의 번호를 키, 입차 시간을 값으로 저장
    out_dict = dict()  # 출차한 차의 번호를 키, 출차 시간을 값으로 저장

    for record in records:
        time, car_num, state = record.split()

        # 현재 차가 이미 입차된 경우 = 출차해야 하는 경우
        if car_num in in_dict and -1 < in_dict[car_num]:
            if car_num in out_dict:  # 이전에 기록된 시간이 있는 경우 누적 합을 저장
                out_dict[car_num] += make_pretty_time(time) - in_dict[car_num]
            else:  # 처음 출차한 경우
                out_dict[car_num] = make_pretty_time(time) - in_dict[car_num]
            in_dict[car_num] = -1  # 입차 기록 초기화

        else:  # 입차
            in_dict[car_num] = make_pretty_time(time)

    # 입차는 했지만 출차는 하지 않은 차량을 23:59에 출차했다고 가정하여 출차 시간 기록
    for car_num, time in in_dict.items():
        if time == -1:
            continue
        if car_num in out_dict:
            out_dict[car_num] += make_pretty_time("23:59") - in_dict[car_num]
        else:
            out_dict[car_num] = make_pretty_time("23:59") - in_dict[car_num]

    # 주차 요금 계산
    for car_num, time in out_dict.items():
        total_fee = fees[1]
        if fees[0] < time:
            total_fee += (time - fees[0] + fees[2] - 1) // fees[2] * fees[3]  # 올림 처리 포함
        answer.append((car_num, total_fee))  # 차량 번호화 주차 요금 기록

    answer.sort()  # 차량 번호를 기준으로 정렬
    answer = [fee for _, fee in answer]  # 차량 번호 제거
    return answer
