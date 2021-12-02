# 14868. 문명


import sys
from collections import deque


def find(x):
    if parents[x] == x:
        return x

    p_x = find(parents[x])
    parents[x] = p_x
    return p_x


def union(x, y):
    p_x = find(x)
    p_y = find(y)
    parents[p_y] = p_x


def bfs():
    global civilization_cnt

    year = 0
    while q:
        year += 1  # 햇수 증가
        for _ in range(len(q)):
            r, c = q.popleft()
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if nr < 1 or N < nr or nc < 1 or N < nc:
                    continue
                if civil[nr][nc] == 0:  # 문명이 아닌 지역
                    q.append((nr, nc))
                    civil[nr][nc] = civil[r][c]

                    # 인접한 지역의 문명 존재 여부 확인
                    for nd in range(4):
                        nnr, nnc = nr + dr[nd], nc + dc[nd]
                        if nnr < 1 or N < nnr or nnc < 1 or N < nnc:
                            continue
                        if civil[nnr][nnc] == 0:  # 문명이 없다면 무시
                            continue

                        # 다른 문명이 존재하는데 이미 융합된 문명이 아닐 경우 결합
                        if civil[nr][nc] != civil[nnr][nnc] and find(civil[nnr][nnc]) != find(civil[nr][nc]):
                            union(civil[r][c], civil[nnr][nnc])
                            civilization_cnt -= 1
                            if civilization_cnt == 1:
                                return year

                # 다른 문명을 만났는데 이미 융합된 문명이 아닐 경우 결합
                elif civil[nr][nc] != civil[r][c] and find(civil[nr][nc]) != find(civil[r][c]):
                    union(civil[r][c], civil[nr][nc])
                    civilization_cnt -= 1
                    if civilization_cnt == 1:
                        return year
                    q.append((nr, nc))


def initial_bfs():
    global civilization_cnt

    # 시작부터 문명끼리 붙어있는지 아닌지 검사
    while initial_q:
        r, c = initial_q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 1 or N < nr or nc < 1 or N < nc:
                continue

            # 문명이 붙어있는 경우 문명 개수를 줄이고 만약 전부 붙어있다면 False 반환
            if civil[nr][nc] and find(civil[nr][nc]) != find(civil[r][c]):
                union(civil[r][c], civil[nr][nc])
                civilization_cnt -= 1
                if civilization_cnt == 1:
                    return False
    return True


N, K = map(int, input().split())
parents = [0] + list(range(1, K + 1))  # 각 문명의 조상 문명 기록
civil = [[0] * (N + 1) for _ in range(N + 1)]  # 각 문명의 번호 기록
civilization_cnt = 0  # 총 문명 개수

dr = (-1, 1, 0, 0)  # 상하좌우
dc = (0, 0, -1, 1)

q = deque()
initial_q = deque()  # initial_bfs()에서 사용할 덱
for _ in range(K):
    row, col = map(int, sys.stdin.readline().split())
    q.append((row, col))
    initial_q.append((row, col))
    civilization_cnt += 1
    civil[row][col] = civilization_cnt

if initial_bfs():
    print(bfs())
else:
    print(0)