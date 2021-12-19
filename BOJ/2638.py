# 2638. 치즈


import sys
from collections import deque


def find_air_area(t):
    # bfs로 (0, 0) 지점에서 시작해 현재 시간 t에서 도달할 수 있는
    # 지역의 값을 (t + 1)로 설정
    q = deque()
    q.append((0, 0))
    cheese_map[0][0] = t + 1
    while q:
        cur_r, cur_c = q.popleft()
        for direction in range(4):
            next_r, next_c = cur_r + dr[direction], cur_c + dc[direction]
            if next_r < 0 or N <= next_r or next_c < 0 or M <= next_c:
                continue
            if cheese_map[next_r][next_c] == t + 1:  # 이미 방문한 지역
                continue
            if cheese_map[next_r][next_c] == 1:
                continue
            cheese_map[next_r][next_c] = t + 1
            q.append((next_r, next_c))


N, M = map(int, sys.stdin.readline().split())
cheese_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cheese_set = set()  # 치즈 좌표 저장 세트
for row in range(N):
    for col in range(M):
        if cheese_map[row][col]:  # 치즈 발견
            cheese_set.add((row, col))

dr = (-1, 1, 0, 0)  # 상하좌우 델타 행
dc = (0, 0, -1, 1)  # 상하좌우 델타 열

time = 0
while cheese_set:  # 치즈가 모두 녹을때 까지 반복
    time += 1
    find_air_area(time)  # 현재 도달 가능 공기 지역 기록
    melted_cheese_set = set()  # 녹은 치즈의 좌표 저장 세트
    for cheese_r, cheese_c in cheese_set:
        air_cnt = 0  # 사방에 있는 도달 가능 공기의 수
        for d in range(4):
            nr, nc = cheese_r + dr[d], cheese_c + dc[d]
            if nr < 0 or N <= nr or nc < 0 or M <= nc:
                continue
            
            # 현재 도달 가능 공기를 만난 경우 
            if cheese_map[nr][nc] == time + 1:
                air_cnt += 1
        
        # 만약 2변 이상이 공기와 접한 경우 녹은 치즈 처리
        if 2 <= air_cnt:
            melted_cheese_set.add((cheese_r, cheese_c))
    
    # 녹은 치즈에 대해 좌표 값을 변경
    for cheese_r, cheese_c in melted_cheese_set:
        cheese_map[cheese_r][cheese_c] = time + 1
    cheese_set -= melted_cheese_set  # 녹은 치즈 제거
print(time)