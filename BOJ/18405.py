# 18405. 경쟁적 전염


N, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

time = 1
Q = []

for i in range(N):
    for j in range(N):
        if MAP[i][j]:
            Q.append((MAP[i][j], i, j, time))

Q.sort()

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

while len(Q) > 0:
    now = Q.pop(0)
    now_r, now_c = now[1], now[2]
    time = now[3]

    # time에 2가 들어있다면 1번 time이 다 끝난 상태
    # 따라서 S time이 다 끝났다면 현재 time은 S+1
    if time == S + 1:
        break

    for k in range(4):
        nr, nc = now_r + di[k], now_c + dj[k]

        if nr < 0 or nc < 0 or N <= nr or N <= nc:
            continue
        if MAP[nr][nc] > 0:
            continue

        Q.append((now[0], nr, nc, time + 1))
        MAP[nr][nc] = MAP[now_r][now_c]

print(MAP[X-1][Y-1])


'''
처음 시도할 때에는 Q를 정렬하지 않고 조건문을 아래와 같이 추가하였다.

if MAP[nr][nc] < MAP[now_r][now_c] and MAP[nr][nc] != 0:
    continue
if MAP[nr][nc] > MAP[now_r][now_c]:
    continue
      
만약 다음에 갈 칸이 현재 칸보다 숫자가 작으면서 0이 아니라면 넘어가고
만약 다음에 갈 칸이 현재 칸보다 숫자가 크면 넘어가고.

이렇게 하니 시간이 초과된다.

조건문을 수정하니 통과될 수 있었다.
'''