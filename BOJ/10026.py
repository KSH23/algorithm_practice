# 10026 적록색약


# 현재 위지와 숫자를 받으면 해당 위치를 중심으로 bfs를 이용해
# 현재 위치 색과 같은 지점들의 visited 값을 num으로 채움
def paint(row, col, num):
    di = [-1, 1, 0, 0]    # 상하좌우
    dj = [0, 0, -1, 1]

    queue = [[row, col]]    # 큐 생성
    cur_color = PHOTO[row][col]    # 현재 색상

    while len(queue) > 0:
        now = queue.pop(0)
        now_r, now_c = now[0], now[1]
        for k in range(4):
            nr, nc = now_r + di[k], now_c + dj[k]
            if nr < 0 or nc < 0 or N <= nr or N <= nc:
                continue
            if visited[nr][nc] > 0:
                continue
            if PHOTO[nr][nc] == cur_color:    # 색이 같은 경우에만
                queue.append([nr, nc])
                visited[nr][nc] = num    # 매개변수로 들어온 숫자 할당


N = int(input())    # 그림의 크기
PHOTO = [list(input()) for _ in range(N)]    # 그림
ans = [0, 0]    # 적록색약이 아닐 때 구역 수[0]와 적록색약일 때 구역 수[1]

for repeat in range(2):    # 적록색약 아닐 때, 맞을 때, 총 두 번 반벅
    # 만약 repeat가 1이면 적록색약일 때이며, PHOTO를 적록색약이 보는 그림으로 아예 바굼
    if repeat:
        for i in range(N):
            for j in range(N):
                if PHOTO[i][j] == 'G':
                    PHOTO[i][j] = 'R'

    visited = [[0] * N for _ in range(N)]
    cur_num = 1

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = cur_num
                paint(i, j, cur_num)
                # 한 번의 구역 체크가 끝나면 cur_num을 1 추가함
                cur_num += 1

    # 완성된 visited에서 가장 큰 수를 찾으면 그 값이 구역의 수
    for i in range(N):
        for j in range(N):
            if visited[i][j] > ans[repeat]:
                # ans에 적록색약 아닐 때, 맞을 때가 순서대로 담김
                ans[repeat] = visited[i][j]

print(f'{ans[0]} {ans[1]}')