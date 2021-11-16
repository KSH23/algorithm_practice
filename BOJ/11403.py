# 11403. 경로 찾기


import sys
from collections import deque


def bfs(start_node, end_node):
    q = deque()
    q.append(end_node)

    while q:
        # 현재 도착 노드
        c_end_node = q.popleft()

        for next_node in range(N):
            # 갈 수 있는 다음 노드 탐색
            if MAP[c_end_node][next_node]:
                # 탐색한 적 있는 노드는 제외
                if visited[start_node][next_node]:
                    continue

                # 방문 표시
                visited[start_node][next_node] = 1
                visited[c_end_node][next_node] = 1

                # 시작 노드와 도착 노드가 같은 경우는 덱에 추가 안함
                if start_node == next_node:
                    continue
                q.append(next_node)


N = int(sys.stdin.readline())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

for row in range(N):
    for col in range(N):
        if MAP[row][col]:  # 경로 발견
            visited[row][col] = 1
            bfs(row, col)

for visited_row in visited:
    print(' '.join(map(str, visited_row)))