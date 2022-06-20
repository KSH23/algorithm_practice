# 76503. 모두 0으로 만들기


import sys

sys.setrecursionlimit(300000)


def solution(a, edges):
    length = len(a)
    visited = [False] * length  # 방문 표시
    graph = [[] for _ in range(length)]  # node간 연결 그래프
    for node1, node2 in edges:
        graph[node1].append(node2)
        graph[node2].append(node1)

    def dfs(node):
        count = 0  # 현재 node에서 진행하는 행동 횟수

        for next_node in graph[node]:
            if visited[next_node]:
                continue

            visited[next_node] = True  # 방문하지 않은 node에 방문

            # 다음 노드에서 사용한 행동 횟수 + 다음 노드를 0으로 만들기 위해 필요한 행동 횟수
            count += dfs(next_node) + abs(a[next_node])
            a[node] += a[next_node]  # 현재 노드 가중치 갱신

            visited[next_node] = False  # 방문 해제

        return count

    visited[0] = True  # 시작 노드
    result = dfs(0)
    if a[0] == 0:  # 가중치를 모두 0으로 만든 경우
        return result
    return -1
