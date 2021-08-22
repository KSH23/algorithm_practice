# 4963. 섬의 개수(dfs를 반복문으로 구성한 코드)


def dfs(i, j):
    di = [-1, -1, 0, 1, 1, 1, 0, -1]    # 시계방향으로 12시부터 순서대로
    dj = [0, 1, 1, 1, 0, -1, -1, -1]

    stack = [[i, j]]

    while len(stack) > 0:
        for k in range(8):
            # 만약 마지막 스택 좌표 값에서 한 번 전진한 좌표가 지도를 벗어나면 continue로 무시
            if stack[-1][0] + di[k] >= h or stack[-1][0] + di[k] < 0 or stack[-1][1] + dj[k] >= w or stack[-1][1] + dj[k] < 0:
                continue
            # 만약 마지막 스택 좌표 값에서 한 번 전진한 좌표가 바다이거나 이미 방문한 곳이라면 continue로 무시
            if MAP[stack[-1][0] + di[k]][stack[-1][1] + dj[k]] == 0 or visited[stack[-1][0] + di[k]][stack[-1][1] + dj[k]] == 1:
                continue

            # 위 두 조건을 모두 만족하지 않는다면 다음 좌표를 할당하고 스택에 추가한 후 방문한 곳으로 기록
            next_r = stack[-1][0] + di[k]
            next_c = stack[-1][1] + dj[k]
            stack += [[next_r, next_c]]
            visited[next_r][next_c] = 1
            break

        # 지금 내가 도착한 좌표에서 더 갈 수 있는 곳이 있는지 검사
        cnt = 0
        for k in range(8):
            # 만약 도착한 좌표에서 한 칸 전진한 좌표가 지도를 벗어나면 continue로 무시
            if stack[-1][0] + di[k] >= h or stack[-1][0] + di[k] < 0 or stack[-1][1] + dj[k] >= w or stack[-1][1] + dj[k] < 0:
                continue
            # 만약 도착한 좌표에서 한 칸 전진한 좌표가 섬인데 방문한 적 없다면 cnt를 1로 만듦
            if MAP[stack[-1][0] + di[k]][stack[-1][1] + dj[k]] == 1 and visited[stack[-1][0] + di[k]][stack[-1][1] + dj[k]] == 0:
                cnt = 1

        # 만약 cnt가 1이 되지 않았다면 도착한 좌표에서 한 칸 전진할 수 있는 곳이 없다는 것이므로 스택에서 좌표 제거
        if cnt == 0:
            stack.pop()


while True:
    w, h = map(int, input().split())

    if w == 0:
        break

    MAP = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    ans = 0
    for i in range(h):
        for j in range(w):
            if MAP[i][j] == 0 or visited[i][j] == 1:
                continue
            visited[i][j] = 1
            dfs(i, j)    # dfs 함수가 작동한 횟수와 섬의 갯수는 동일
            ans += 1

    print(ans)