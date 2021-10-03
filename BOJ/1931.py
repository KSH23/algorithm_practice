# 1931. 회의실 배정


import sys


N = int(input())
meeting_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 회의 시간을 끝나는 시간 기준으로 정렬, 같은 것이 있으면 시작 시간 기준으로 정렬
meeting_list.sort(key=lambda x: (x[1], x[0]))

meeting_cnt = 1  # 회의 개수
current_idx = 0  # 현재 회의의 인덱스
current_meeting = meeting_list[0]  # 현재 회의

while True:
    for i in range(current_idx + 1, N):
        # 만약 현재 회의 끝나는 시간보다 같거나 크다면 선택
        if current_meeting[1] <= meeting_list[i][0]:
            current_meeting = meeting_list[i]
            current_idx = i
            meeting_cnt += 1
            break
    else:  # 만약 회의를 하나도 선택하지 못했다면 종료
        break

print(meeting_cnt)