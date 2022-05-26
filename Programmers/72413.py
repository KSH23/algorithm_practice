# 72413. 합승 택시 요금


def solution(n, s, a, b, fares):

    # 요금을 2차원 배열로 정리
    cost = [[100000 * n] * (n + 1) for _ in range(n + 1)]
    for node in range(1, n + 1):
        cost[node][node] = 0
    for node_1, node_2, fare in fares:
        cost[node_1][node_2] = fare
        cost[node_2][node_1] = fare

    # 플로이드-와샬 알고리즘으로 각 지점간 최소 요금 기록
    for via in range(1, n + 1):
        for start in range(1, n + 1):
            for end in range(1, n + 1):
                cost[start][end] = min(cost[start][end], cost[start][via] + cost[via][end])

    answer = cost[s][a] + cost[s][b]  # 합승을 하지 않는 경우
    for via in range(1, n + 1):
        # 각 경유 지점을 탐색하며 최소 요금 갱신
        answer = min(answer, cost[s][via] + cost[via][a] + cost[via][b])

    return answer
