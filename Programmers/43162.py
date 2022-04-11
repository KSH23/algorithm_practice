# 43162. 네트워크


from collections import deque


def solution(n, computers):
    # 단방향 그래프가 주어질 경우를 대비해 간선 그래프를 생성
    edges = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                edges[i][j] = True
                edges[j][i] = True

    visited = [False] * n  # 방문한 노드 표시
    dq = deque(list(range(n)))
    answer = 0  # 네트워크 수
    while dq:
        node = dq.popleft()
        if not visited[node]:  # 처음 만나는 노드의 경우 새 네트워크로 기록
            visited[node] = True
            answer += 1

        for next_node in range(n):  # 연결된 노드에 대하여 방문표시 및 덱에 추가
            if edges[node][next_node] and not visited[next_node]:
                dq.appendleft(next_node)
                visited[next_node] = True

    return answer
