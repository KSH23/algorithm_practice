# 1913. 달팽이


N = int(input())
target = int(input())    # 찾기를 원하는 숫자

GRID = [[0] * N for _ in range(N)]

di = [1, 0, -1, 0]    # row의 하 우 상 좌
dj = [0, 1, 0, -1]    # col의 하 우 상 좌

num = N**2   # 채울 숫자
i, j = -1, 0    # 현재 위치(i, j) 초기화
k = 0    # 현재 방향 초기화

ans_r = ans_c = 0    # 원하는 값을 찾으면 그 떄의 좌표를 저장할 변수

while num > 0:
    # 만약 다음에 갈 좌표가 GRID를 벗어나지 않고 아직 값이 할당되지 않았다면
    if 0 <= i + di[k] < N and 0 <= j + dj[k] < N and GRID[i + di[k]][j + dj[k]] == 0:
        i = i + di[k]    # 다음 좌표로 이동하고
        j = j + dj[k] 
        GRID[i][j] = num    # 값을 할당한 후
        if num == target:    # 찾던 값이 등장하면 그 때의 좌표를 저장
            ans_r, ans_c = i, j
        num -= 1
    else:    # GRID 밖으로 가거나 이미 값이 할당된 좌표를 만나면 방향 전환
        k = (k + 1) % 4

for i in range(N):
    print(' '.join(map(str, GRID[i])))
print('{} {}'.format(ans_r + 1, ans_c + 1))