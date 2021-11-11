# 1932. 정수 삼각형


import sys


def dfs(idx, row):
    if row == N - 1:  # 마지막 줄 도달
        memo[row][idx] = tri[row][idx]
        return tri[row][idx]

    if memo[row][idx] > -1:  # 이미 탐색이 완료된 좌표인 경우
        return memo[row][idx]

    # 현재 index에서 갈 수 있는 다음 인덱스는 index, index + 1
    ret = max(dfs(idx, row + 1), dfs(idx + 1, row + 1))
    ret += tri[row][idx]  # 현재 좌표 값 추가

    memo[row][idx] = ret
    return ret


N = int(sys.stdin.readline())
tri = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
memo = [[-1] * N for _ in range(N)]  # 해당 좌표에서 내려가 만들 수 있는 최대 값 저장
dfs(0, 0)
print(memo[0][0])