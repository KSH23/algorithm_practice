# 17070. 파이프 옮기기 1


import sys


N = int(input())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# pipe 리스트는 가로, 세로, 대각선 파이프가 오는 경우의 수를 담음
# 이때 인덱스는 [가로, 세로, 대각선]을 의미
pipe = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
pipe[0][1] = [1, 0, 0]    # 가장 처음 놓인 파이프 설정

for r in range(0, N):
    for c in range(2, N):
        if MAP[r][c]:    # 벽은 넘어감
            continue
        if 0 <= c - 1 < N:    # 맵을 벗어나지 않는 한해서
            # 가로로 올 수 있는 파이프는 좌측에 있는 가로, 대각선 파이프
            pipe[r][c][0] = pipe[r][c - 1][0] + pipe[r][c - 1][2]
        if 0 <= r - 1 < N:
            # 세로로 올 수 있는 파이프는 위에 있는 세로, 대각선 파이프
            pipe[r][c][1] = pipe[r - 1][c][1] + pipe[r - 1][c][2]
        if 0 <= c - 1 < N and 0 <= r - 1 < N:
            # 대각선으로 올 때에는 좌측, 위쪽에 벽이 있으면 안됨
            if MAP[r - 1][c] == 1 or MAP[r][c - 1] == 1:
                continue
            # 대각선으로 올 수 있는 파이프는 좌상에 있는 모든 파이프
            pipe[r][c][2] = sum(pipe[r - 1][c - 1])

print(sum(pipe[N-1][N-1]))