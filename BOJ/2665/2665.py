# 2665. 미로만들기


n = int(input())    # 정사각형 맵의 크기
MAP = [list(map(int, input())) for _ in range(n)]    # 맵

min_cost_map = [[0] * n for _ in range(n)]    # 최소 비용 저장 맵
min_cost_map[0][0] = 1    # 시작방의 최소 비용을 1로 설정

di = [-1, 1, 0, 0]    # 상하좌우
dj = [0, 0, -1, 1]    # 상하좌우
Q = [(0, 0)]    # 큐 생성

while len(Q) > 0:    # BFS
    now = Q.pop(0)
    now_r, now_c = now[0], now[1]    # 현재 방의 행과 열

    for k in range(4):
        # 다음에 갈 수 있는 방은 맵을 벗어나지 않고 최소 비용이 계산되지 않은 방
        nr, nc = now_r + di[k], now_c + dj[k]
        if nr < 0 or nc < 0 or n <= nr or n <= nc:
            continue
        if min_cost_map[nr][nc] > 0:
            continue

        # 다음 방에 현재 방의 비용을 할당
        min_cost_map[nr][nc] = min_cost_map[now_r][now_c]

        # 만약 벽이었다면 비용이 1 증가하고 큐의 오른쪽에 방을 추가
        if MAP[nr][nc] == 0:
            min_cost_map[nr][nc] += 1
            Q += [(nr, nc)]
        else:    # 벽이 아니었다면 큐의 왼쪽에 방을 추가
            Q = [(nr, nc)] + Q

print(min_cost_map[n-1][n-1] - 1)