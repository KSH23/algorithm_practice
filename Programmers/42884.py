# 42884. 단속카메라


def solution(routes):
    routes.sort(key=lambda x: x[1])  # 진출 지점 기준으로 정렬

    answer = 0
    last_camera = -30001  # 가장 마지막에 설치된 카메라의 위치

    for enter, out in routes:
        # 현재 차량이 가장 마지막에 설치된 카메라를 만나는 경우 무시
        if enter <= last_camera <= out:
            continue

        # 현재 차량이 카메라를 못 만난 경우 카메라를 설치
        last_camera = out
        answer += 1

    return answer
