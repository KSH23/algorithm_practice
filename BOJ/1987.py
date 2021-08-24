# 1987. 알파벳


import sys


def dfs(row, col, cnt):
    global ans

    di = [-1, 1, 0, 0]  # 상하좌우
    dj = [0, 0, -1, 1]  # 상하좌우

    # visited[row][col] = 1
    check[ord(MAP[row][col])] = 1

    for k in range(4):
        if row + di[k] >= R or col + dj[k] >= C or row + di[k] < 0 or col + dj[k] < 0:
            continue
        if check[ord(MAP[row + di[k]][col + dj[k]])] == 1:
            continue

        dfs(row + di[k], col + dj[k], cnt + 1)
    # visited[row][col] = 0
    check[ord(MAP[row][col])] = 0

    if cnt > ans:
        ans = cnt


R, C = map(int, sys.stdin.readline().split())

# 문자열을 쪼개 리스트로 변환하면 이후 ord() 사용할때 파이참이 경고함
# 문자 1개가 아닌 문자열이 들어올 수 있는 가능성이 생기는 코드이기 때문에
MAP = [sys.stdin.readline() for _ in range(R)]
# visited = [[0] * C for _ in range(R)]
check = [0] * 256

ans = 0
dfs(0, 0, 1)
print(ans)