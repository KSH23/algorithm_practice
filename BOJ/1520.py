# 1520. 내리막 길


import sys
limit_number = 30000
sys.setrecursionlimit(limit_number)


def dfs(r, c):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    if r == M-1 and c == N-1:    # 목적지에 도달하면 1을 반환
        return 1
    if dp[r][c] != -1:    # 이미 경로 계산이 끝난 지점이면 해당 값을 반환
        return dp[r][c]

    # [i][j] 지점에서 갈 수 있는 상하좌우를 모두 탐색
    # 각 탐색에서 위 두 if문을 만족시키면 해당 값을 가지고 돌아오지만
    # 그렇지 않다면 최초로 cnt에 할당된 0을 dp[i][j]에 넣게 될 것
    # 따라서 dp 리스트는 처음 -1로 초기화 되어야 하며
    # cnt는 += 연산자를 통해 값이 계속 늘어나야 함
    cnt = 0
    for i in range(4):
        next_r = r + di[i]
        next_c = c + dj[i]
        if next_r < 0 or next_c < 0 or next_r >= M or next_c >= N:
            continue
        if MAP[r][c] <= MAP[next_r][next_c]:
            continue
        cnt += dfs(next_r, next_c)

    dp[r][c] = cnt

    return cnt


M, N = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(M)]

# dp[i][j]는 MAP[i][j]에서 MAP[M-1][N-1]로 갈 수 있는 경우의 수를 담음
dp = [[-1] * N for _ in range(M)]
dp[M-1][N-1] = 1

dfs(0, 0)
print(dp[0][0])
