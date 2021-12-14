# 42586. 기능개발


def solution(progresses, speeds):
    answer = []

    # 각 인덱스에 해당하는 일이 끝나는 날짜를 기록
    work_done = [0] * len(progresses)

    for idx in range(len(progresses)):
        # 배포까지 필요한 날짜
        left_time = (100 - progresses[idx]) // speeds[idx]
        # 날짜 올림 처리
        if (100 - progresses[idx]) % speeds[idx]:
            left_time += 1

        # 이전 작업이 끝나지 않은 경우
        if 0 < idx and left_time <= work_done[idx - 1]:
            # 현재 작업의 배포 날짜는 이전 작업의 배포 날짜와 같다
            work_done[idx] = work_done[idx - 1]
            answer[-1] += 1

        # 이번 작업이 바로 배포될 수 있는 경우
        else:
            answer.append(1)
            work_done[idx] = left_time

    return answer