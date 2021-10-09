# 14502. 연구소


import sys
from collections import deque


def bfs(virus_deque):
    q = virus_deque.copy()  # 바이러스 deque 얕은 복사

    dr = [-1, 1, 0, 0]  # 상하좌우
    dc = [0, 0, -1, 1]

    visited = [[0] * C for _ in range(R)]
    for v in q:
        visited[v[0]][v[1]] = 1  # 초기 바이러스 방문 표시
    virus_num = 0  # 바이러스 개수

    while q:
        cur = q.popleft()
        row, col = cur[0], cur[1]
        virus_num += 1
        for d in range(4):
            nr, nc = row + dr[d], col + dc[d]
            if nr < 0 or nc < 0 or R <= nr or C <= nc:
                continue
            if lab[nr][nc] == 1 or visited[nr][nc] == 1:
                continue
            visited[nr][nc] = 1
            q.append((nr, nc))

    return virus_num


R, C = map(int, input().split())
lab = []  # 연구실
virus = deque()  # 바이러스 deque
safe_num = 0  # 안전 영역 개수
safe_places = []  # 안전 영역 좌표 저장
for r in range(R):
    temp = list(map(int, sys.stdin.readline().split()))
    for c in range(C):
        if temp[c] == 2:
            virus.append((r, c))
        elif temp[c] == 0:
            safe_num += 1
            safe_places.append((r, c))
    lab.append(temp)

# 최종 안전 영역의 개수는 이후 세워질 세 개의 벽을 빼고
# 총 바이러스의 개수를 뺄 것이므로 처음 고려하지 않은 바이러스 개수를 더함
safe_num = safe_num - 3 + len(virus)

ans = 0  # 최종 정답

# 모든 안전 영역 중 3개를 골라 벽을 세우는 for loop
for idx1 in range(0, len(safe_places)):
    lab[safe_places[idx1][0]][safe_places[idx1][1]] = 1
    for idx2 in range(idx1 + 1, len(safe_places)):
        lab[safe_places[idx2][0]][safe_places[idx2][1]] = 1
        for idx3 in range(idx2 + 1, len(safe_places)):
            lab[safe_places[idx3][0]][safe_places[idx3][1]] = 1
            ans = max(ans, safe_num - bfs(virus))  # 정답 갱신
            lab[safe_places[idx3][0]][safe_places[idx3][1]] = 0
        lab[safe_places[idx2][0]][safe_places[idx2][1]] = 0
    lab[safe_places[idx1][0]][safe_places[idx1][1]] = 0

print(ans)