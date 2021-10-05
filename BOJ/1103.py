# 1103. 게임


import sys


sys.setrecursionlimit(100000000)


def dfs(row, col):
    if dp[row][col]:
        return dp[row][col]

    result = 1
    x = int(BOARD[row][col])  # 이동 거리
    for d in range(4):
        nr, nc = row + dr[d] * x, col + dc[d] * x
        if nr < 0 or nc < 0 or N <= nr or M <= nc or BOARD[nr][nc] == 'H':
            continue
        if visited[nr][nc]:  # 방문했던 곳에 다시 방문하면 무한반복이므로 중단
            return -1

        visited[nr][nc] = 1
        temp_result = dfs(nr, nc)
        if temp_result == -1:  # 무한반복 결과가 나온 경우
            return -1
        result = max(result, temp_result + 1)
        visited[nr][nc] = 0

    dp[row][col] = result
    return result


N, M = map(int, input().split())
BOARD = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

dr = [-1, 1, 0, 0]  # 상하좌우
dc = [0, 0, -1, 1]

visited = [[0] * M for _ in range(N)]
dp = [[0] * M for _ in range(N)]  # dp[i][j]: (i, j)에서 갈 수 있는 최대 경로

print(dfs(0, 0))