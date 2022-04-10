# 49189. 가장 먼 노드


from collections import deque


def solution(n, vertex):
    answer = 0
    edges = [[] for _ in range(n + 1)]  # 간선 저장 리스트
    for v1, v2 in vertex:
        edges[v1].append(v2)
        edges[v2].append(v1)
    
    visited = [False] * (n + 1)  # 방문 기록 리스트

    visited[1] = True  # 초기 방문 설정
    dq = deque([1])  # 초깃값 설정
    while dq:
        # 같은 깊이에 있는 노드의 수는 dq를 한 번 탐색할 때 추가되는 노드의 수
        # 같은 깊이에 있는 노드의 수를 계속 갱신하면 가장 마지막 깊이에 도달하고,
        # 결국가장 마지막 깊이의 노드의 수로 갱신됨
        answer = len(dq)
        for _ in range(len(dq)):
            node = dq.popleft()
            for next_node in edges[node]:  # 갈 수 있는 노드
                if visited[next_node]:
                    continue
                visited[next_node] = True
                dq.append(next_node)
            
    return answer