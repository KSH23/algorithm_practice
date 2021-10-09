# 21608. 상어 초등학교


import sys


N = int(input())
students = {}  # 학생을 key, 좋아하는 학생 목록을 value로 받을 딕셔너리
for _ in range(N ** 2):
    temp_student = list(map(int, sys.stdin.readline().split()))
    students[temp_student[0]] = temp_student[1:]
classroom = [[0] * N for _ in range(N)]  # 학생이 들어올 교실

dr = [-1, 1, 0, 0]  # 상하좌우
dc = [0, 0, -1, 1]

# 각 학생의 자리를 지정할 for loop
for student, wanted_students in students.items():
    seat = []  # 최종 자리 저장 변수

    # 인접한 좋아하는 친구와 비어있는 자리가 모두 0이 될 경우를 고려하여
    # 최대 인접한 좋아하는 학생 수와 비어있는 자리 수의 초기값을 -1로 설정
    max_wanted_cnt = -1  # 최대 인접한 좋아하는 학생 수
    max_empty_cnt = -1  # 최대 인접한 비어있는 자리 수
    for r in range(N):
        for c in range(N):
            if classroom[r][c] > 0:
                continue  # 이미 사람이 있으면 통과

            wanted_cnt = 0  # 인접한 좋아하는 학생 수
            empty_cnt = 0  # 인접한 비어있는 자리 수
            for d in range(4):  # 현재 자리 (r, c)에서 상하좌우 검사
                nr, nc = r + dr[d], c + dc[d]
                if nr < 0 or nc < 0 or N <= nr or N <= nc:
                    continue
                if classroom[nr][nc] == 0:
                    empty_cnt += 1
                elif classroom[nr][nc] in wanted_students:
                    wanted_cnt += 1

            # 최대 인접 좋아하는 학생 수가 갱신되는 경우
            if max_wanted_cnt < wanted_cnt:
                seat = [r, c]  # 자리 갱신
                max_wanted_cnt = wanted_cnt
                max_empty_cnt = empty_cnt

            # 최대 인접 좋아하는 학생 수가 동일한 경우
            elif max_wanted_cnt == wanted_cnt:
                # 기존의 최대 비어있는 자리 수보다 큰 경우만 갱신
                if max_empty_cnt < empty_cnt:
                    seat = [r, c]  # 자리 갱신
                    max_empty_cnt = empty_cnt

    classroom[seat[0]][seat[1]] = student  # 최종 자리 설정

# 학생과 인접한 좋아하는 학생의 수를 세기 위한 작업 진행
seat_info = [[0] * N for _ in range(N)]  # 인접한 좋아하는 학생 수 저장
for r in range(N):
    for c in range(N):
        s = classroom[r][c]
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nc < 0 or N <= nr or N <= nc:
                continue
            if classroom[nr][nc] in students[s]:
                seat_info[r][c] += 1

ans = 0  # 최종 정답
for r in range(N):  # 학생의 만족도를 조사하는 for loop
    for c in range(N):
        if seat_info[r][c] == 0:
            continue
        ans += 10 ** (seat_info[r][c] - 1)

print(ans)