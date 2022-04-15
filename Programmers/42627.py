# 42627. 디스크 컨트롤러


import heapq


def solution(jobs):
    answer, length = 0, len(jobs)
    jobs.sort()  # 작업 요청 시간 기준 정렬

    time = 0  # 현재 시각
    while jobs:
        start, duration = heapq.heappop(jobs)  # 현재 작업

        if time < start:  # 아직 작업 요청이 들어오기 이전인 경우
            time = start  # 작업 요청 시각으로 이동
        time += duration  # 작업 완료
        answer += time - start  # 소요 시간 기록

        possible_jobs = []  # 현재 작업중 들어온 요청을 저장할 리스트
        while jobs and jobs[0][0] <= time:
            # 소요시간 기준으로 오름차순 정렬되게 possible_jobs에 추가
            start, duration = heapq.heappop(jobs)
            heapq.heappush(possible_jobs, [duration, start])

        possible_jobs = [[x[1], x[0]] for x in possible_jobs]  # 원소 위치 변경
        jobs = possible_jobs + jobs

    return answer // length
