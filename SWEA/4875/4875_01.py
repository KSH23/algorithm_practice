# 4875. 미로(BFS)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().rstrip())) for _ in range(N)]
    q = []
    check = [[0] * N for _ in range(N)]
    ans = 0

    now_row = now_col = 0
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 2:
                now_row = i
                now_col = j

    q.append((now_row, now_col))
    check[now_row][now_col] = 1

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    while q:
        now = q.pop(0)
        now_row = now[0]
        now_col = now[1]
        if MAP[now_row][now_col] == 3:
            ans = 1

        for k in range(4):
            next_row = now_row + di[k]
            next_col = now_col + dj[k]

            if next_row < 0 or N <= next_row or next_col < 0 or N <= next_col:
                continue
            if MAP[next_row][next_col] == 1:
                continue
            if check[next_row][next_col] == 1:
                continue

            check[next_row][next_col] = 1
            q.append((next_row, next_col))

    print('#{} {}'.format(tc, ans))