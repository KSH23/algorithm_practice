# 1005. ACM Craft


import sys


sys.setrecursionlimit(10000)


def get_time(b_num):
    # b_num: 현재 지으려 하는 건물 번호
    if -1 < memo[b_num]:  # 이미 계산된 경우
        return memo[b_num]

    ret = times[b_num]  # 현재 건물의 건설 시간
    
    # 우선적으로 지어져야 하는 건물이 있는 경우 그 건물들 중
    # 최장 건설시간을 총 건설 시간에 추가
    if requirements[b_num]:
        # rb_num: required building number 먼저 지어져야 하는 건물 번호
        ret += max(get_time(rb_num) for rb_num in requirements[b_num])
    
    memo[b_num] = ret  # 기록
    return ret


T = int(sys.stdin.readline())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    
    # 건물을 짓는데 걸리는 시간
    times = [0] + list(map(int, sys.stdin.readline().split()))
    
    # 각 건물을 짓기 위해 필요한 건물 번호를 저장하는 배열
    requirements = [[] for _ in range(N + 1)]
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        requirements[Y].append(X)  # Y가 지어지기 위해선 X가 필요
    W = int(sys.stdin.readline())
    
    # memo[i]: i 건물을 짓기 위해 필요한 최소시간 기록
    memo = [-1] * (N + 1) 
    print(get_time(W))