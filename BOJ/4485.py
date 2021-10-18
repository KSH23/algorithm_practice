# 4485. 녹색 옷 입은 애가 젤다지?


import sys
import heapq


def dijkstra():
    hq = []  # heapq
    heapq.heappush(hq, [cave[0][0], 0, 0])  # 시작 지점 추가
    dist = [[10 * N * N] * N for _ in range(N)]  # 지불해야 하는 비용 저장
    dist[0][0] = cave[0][0]  # 시작 지점 초기화
    visited = [[0] * N for _ in range(N)]  # 방문 확인
    visited[0][0] = 1  # 시작 지점 방문 표시

    dr = [-1, 1, 0, 0]  # 상하좌우 델타 행
    dc = [0, 0, -1, 1]  # 상하좌우 델타 열

    while hq:
        w, r, c = heapq.heappop(hq)  # 현재 위지의 비용과 좌표
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or N <= nr or nc < 0 or N <= nc:
                continue
            if visited[nr][nc]:
                continue

            # 현재 좌표에서 가는 것이 손해라면 무시
            if dist[nr][nc] < cave[nr][nc] + w:
                continue

            dist[nr][nc] = cave[nr][nc] + w  # 비용 갱신
            visited[nr][nc] = 1  # 방문 표시

            if nr == N - 1 and nc == N - 1:  # 도착
                return dist[nr][nc]

            heapq.heappush(hq, [dist[nr][nc], nr, nc])


problem_num = 1
while problem_num:
    N = int(input())  # 동굴의 크기
    if N == 0:
        break  # 0이 입력되면 전체 입력 종료

    cave = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    print(f'Problem {problem_num}: {dijkstra()}')
    problem_num += 1