# 14500. 테트로미노


import sys


N, M = map(int, input().split())
MAP = [[0] * (M + 1)] + [[0] + list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0] * (M + 1) for _ in range(N + 1)]  # (r, c)까지의 총합을 [r][c]에 저장힐 리스트
for r in range(1, N + 1):
    for c in range(1, M + 1):
        dp[r][c] = MAP[r][c] + dp[r - 1][c] + dp[r][c - 1] - dp[r - 1][c - 1]

ans = 0  # 최종 정답
for r in range(1, N + 1):
    for c in range(1, M + 1):
        # 19가지 경우의 수를 모두 하나하나 변수에 저장
        hor = ver = square = L1 = L2 = L3 = L4 = L5 = L6 = L7 = L8 = Z1 = Z2 = Z3 = Z4 = U1 = U2 = U3 = U4 = 0

        # ㅡ 모양
        if 4 <= c:
            hor = dp[r][c] - dp[r - 1][c] - dp[r][c - 4] + dp[r - 1][c - 4]

        # | 모양
        if 4 <= r:
            ver = dp[r][c] - dp[r - 4][c] - dp[r][c - 1] + dp[r - 4][c - 1]

        # ㅁ 모양
        if 2 <= r and 2 <= c:
            square = dp[r][c] - dp[r - 2][c] - dp[r][c - 2] + dp[r - 2][c - 2]

        if 3 <= r and 2 <= c:
            # L 모양 (좌측 세로 세 칸 + 우측 한 칸)
            L1 = dp[r][c - 1] - dp[r - 3][c - 1] - dp[r][c - 2] + dp[r - 3][c - 2] + MAP[r][c]

            # L 거울상 모양 (좌측 한 칸 + 우측 세로 세 칸)
            L2 = MAP[r][c - 1] + dp[r][c] - dp[r - 3][c] - dp[r][c - 1] + dp[r - 3][c - 1]

            # 긴 ㄱ 모양 (좌측 한 칸 + 우측 세로 세 칸)
            L3 = MAP[r - 2][c - 1] + dp[r][c] - dp[r - 3][c] - dp[r][c - 1] + dp[r - 3][c - 1]

            # 긴 ㄱ 거울상 모양 (좌측 세로 세 칸 + 우측 한 칸)
            L4 = dp[r][c - 1] - dp[r - 3][c - 1] - dp[r][c - 2] + dp[r - 3][c - 2] + MAP[r - 2][c]

            # Z같은 번개 모양 (상단 한 칸 + 중간 가로 두 칸 + 하단 한 칸)
            Z1 = MAP[r - 2][c - 1] + dp[r - 1][c] - dp[r - 2][c] - dp[r - 1][c - 2] + dp[r - 2][c - 2] + MAP[r][c]

            # Z같은 번개 거울상 모양 (상단 한 칸 + 중간 가로 두 칸 + 하단 한 칸)
            Z2 = MAP[r - 2][c] + dp[r - 1][c] - dp[r - 2][c] - dp[r - 1][c - 2] + dp[r - 2][c - 2] + MAP[r][c - 1]

            # ㅓ 모양 (좌측 한 칸 + 우측 세로 세 칸)
            U3 = MAP[r - 1][c - 1] + dp[r][c] - dp[r - 3][c] - dp[r][c - 1] + dp[r - 3][c - 1]

            # ㅏ 모양 (좌측 세로 세 칸 + 우측 한 칸)
            U4 = dp[r][c - 1] - dp[r - 3][c - 1] - dp[r][c - 2] + dp[r - 3][c - 2] + MAP[r - 1][c]

        if 2 <= r and 3 <= c:
            # ㅜ 모양 (상단 가로 세 칸 + 하단 한 칸)
            U1 = dp[r - 1][c] - dp[r - 2][c] - dp[r - 1][c - 3] + dp[r - 2][c - 3] + MAP[r][c - 1]

            # ㅗ 모양 (상단 한 칸 + 하단 가로 세 칸)
            U2 = MAP[r - 1][c - 1] + dp[r][c] - dp[r - 1][c] - dp[r][c - 3] + dp[r - 1][c - 3]

            # Z 모양 (좌측 한 칸 + 가운데 세로 두 칸 + 우측 한 칸)
            Z3 = MAP[r - 1][c - 2] + dp[r][c - 1] - dp[r - 2][c - 1] - dp[r][c - 2] + dp[r - 2][c - 2] + MAP[r][c]

            # Z 거울상 모양 (좌측 한 칸 + 가운데 세로 두 칸 + 우측 한 칸)
            Z4 = MAP[r][c - 2] + dp[r][c - 1] - dp[r - 2][c - 1] - dp[r][c - 2] + dp[r - 2][c - 2] + MAP[r - 1][c]

            # 짧은 ㄱ 모양 (상단 세 칸 + 하단 한 칸)
            L5 = dp[r - 1][c] - dp[r - 2][c] - dp[r - 1][c - 3] + dp[r - 2][c - 3] + MAP[r][c]

            # 짧은 ㄱ 거울상 모양 (상단 세 칸 + 하단 한 칸)
            L6 = dp[r - 1][c] - dp[r - 2][c] - dp[r - 1][c - 3] + dp[r - 2][c - 3] + MAP[r][c - 2]

            # ㄴ 모양 (상단 한 칸 + 하단 세 칸)
            L7 = MAP[r - 1][c - 2] + dp[r][c] - dp[r - 1][c] - dp[r][c - 3] + dp[r - 1][c - 3]

            # ㄴ 거울상 모양 (상단 한 칸 + 하단 세 칸)
            L8 = MAP[r - 1][c] + dp[r][c] - dp[r - 1][c] - dp[r][c - 3] + dp[r - 1][c - 3]

        # 19가지 경우의 수 중 최대값을 선정
        max_sum = max(hor, ver, square, L1, L2, L3, L4, L5, L6, L7, L8, Z1, Z2, Z3, Z4, U1, U2, U3, U4)
        if ans < max_sum:
            ans = max_sum

print(ans)