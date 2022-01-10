# 12849. 본대 산책


import sys


sys.setrecursionlimit(1000000)


def dfs(current_building, time):
    # 이미 계산된 경우
    if -1 < memo[current_building][time]:
        return memo[current_building][time]

    # 경우의 수를 모두 더한 후 memo 리스트에 기록
    ret = 0
    for next_building in MAP[current_building]:
        ret += dfs(next_building, time - 1)
    memo[current_building][time] = ret % 1000000007
    return ret % 1000000007


D = int(input())

# 문제의 건물에 인덱스를 지정하고 그에 따른 연결 건물 기록
MAP = {
    0: (1, 7),
    1: (0, 2, 7),
    2: (1, 3, 6, 7),
    3: (2, 4, 6),
    4: (3, 5),
    5: (4, 6),
    6: (2, 3, 5, 7),
    7: (0, 1, 2, 6)
}

# memo[i][j]: 산책을 시작한 지 j 분만에 i 번 건물에 도착하는 경우의 수
memo = [[-1] * (D + 1) for _ in range(8)]
memo[0][0] = 1  # 시작 지점
for building in range(1, 8):
    memo[building][0] = 0
memo[1][1] = memo[7][1] = 1

print(dfs(0, D))