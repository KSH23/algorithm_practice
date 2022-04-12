# 49191. 순위


def solution(n, results):
    answer = 0

    # x가 y를 이긴다면 graph[x][y]에 1 할당
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for result in results:
        graph[result[0]][result[1]] = 1

    # Floyd-Warshall 알고리즘을 이용해 승패 추가 기록
    for mid in range(1, n + 1):
        for start in range(1, n + 1):
            for end in range(1, n + 1):
                if graph[start][mid] and graph[mid][end]:
                    graph[start][end] = 1

    for player in range(1, n + 1):  # 순위를 탐색하려는 참가자
        cnt = 0  # 탐색 가능한 다른 참가자의 수
        for other in range(1, n + 1):  # 다른 참가자
            # player가 이긴 경우와 진 경우의 합
            cnt += graph[player][other] + graph[other][player]
            
        # 다른 모든 참가자들과 지거나 이겼다면 순위를 알 수 있음
        if cnt == n - 1:
            answer += 1

    return answer
