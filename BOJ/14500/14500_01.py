# 14500_01. 테트로미노


# 기존에 dp를 사용한 방법이 계속 중복된 연산을 하고 시간도 오래 걸려 이를 줄이려 하였지만,
# 결과적으로 더 오래 걸리는 코드를 작성하였다.
# 연산에 걸리는 시간에 대해 더 구체적으로 고민할 필요가 있을 것 같다.


import sys


N, M = map(int, input().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# [[2x2], [3x1의 기본형], [1x3의 기본형], [ㄴ의 기본형], [ㄱ의 기본형]]
# [[1개], [7개], [7개], [2개], [2개]]
# [[1개], [하, 좌, 우, 2상좌, 2상우, 1상좌, 1상우], [3좌, 2좌상, 2좌하, 1좌상, 1좌하, 상, 하], [좌하, 상우], [2상좌, 우]]
dr = [[], [1, 0, 0, -2, -2, -1, -1], [0, -1, 1, -1, 1, -1, 1], [1, -1], [-2, 0]]
dc = [[], [0, -1, 1, -1, 1, -1, 1], [-3, -2, -2, -1, -1, 0, 0], [-1, 1], [-1, 1]]

ans = 0  # 최종 정답
for r in range(N):
    for c in range(M):
        if 1 <= r and 1 <= c:
            origin = MAP[r][c] + MAP[r - 1][c] + MAP[r][c - 1] + MAP[r - 1][c - 1]  # ㅁ 모양
            ans = max(ans, origin)

            for d in range(2):  # ㄴ 기본 도형
                nr, nc = r + dr[3][d], c + dc[3][d]
                if nr < 0 or N <= nr or nc < 0 or M <= nc:
                    continue
                ans = max(ans, origin - MAP[r - 1][c - 1] + MAP[nr][nc])

            for d in range(2):  # ㄱ 기본 도형
                nr, nc = r + dr[4][d], c + dc[4][d]
                if nr < 0 or N <= nr or nc < 0 or M <= nc:
                    continue
                ans = max(ans, origin - MAP[r][c - 1] + MAP[nr][nc])

        if 2 <= r:
            origin = MAP[r - 2][c] + MAP[r - 1][c] + MAP[r][c]  # 세로 세 칸

            for d in range(7):
                nr, nc = r + dr[1][d], c + dc[1][d]
                if nr < 0 or N <= nr or nc < 0 or M <= nc:
                    continue
                ans = max(ans, origin + MAP[nr][nc])

        if 2 <= c:
            origin = MAP[r][c - 2] + MAP[r][c - 1] + MAP[r][c]  # 가로 세 칸

            for d in range(7):
                nr, nc = r + dr[2][d], c + dc[2][d]
                if nr < 0 or N <= nr or nc < 0 or M <= nc:
                    continue
                ans = max(ans, origin + MAP[nr][nc])

print(ans)