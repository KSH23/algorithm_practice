# 67259. [카카오 인턴] 경주로 건설


from collections import deque


def solution(board):
    # board의 크기와 각 칸이 가질 수 있는 최대 비용 설정
    n = len(board)
    max_cost = n * n * 600

    # 각 칸에 대하여 각 방향으로 도달했을 때 필요한 최소 비용 저장
    cost = [[[max_cost, max_cost, max_cost, max_cost] for _ in range(n)] for _ in range(n)]
    cost[0][0] = [0, 0, 0, 0]

    # 상하좌우 방향 벡터 설정
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    dq = deque([(0, 0, 1), (0, 0, 3)])  # 시작 지점은 우측과 아래로 향하는 (0, 0) 지점

    while dq:
        row, col, direction = dq.popleft()

        for d in range(4):
            nr, nc = row + dr[d], col + dc[d]

            # 범위 밖 또는 벽을 만난 경우
            if nr < 0 or n <= nr or nc < 0 or n <= nc or board[nr][nc]:
                continue

            # 기본 비용은 100원이며 현재 방향과 다른 경우 코너 생성으로 500원 추가
            next_cost = cost[row][col][direction] + 100
            if direction != d:
                next_cost += 500

            # 최소 비용 갱신
            if next_cost <= cost[nr][nc][d]:
                cost[nr][nc][d] = next_cost
                dq.append((nr, nc, d))

    return min(cost[n - 1][n - 1])
