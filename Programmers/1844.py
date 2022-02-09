# 1844. 게임 맵 최단거리


from collections import deque


def solution(maps):
    dr = (-1, 1, 0, 0)  # 행의 상하좌우
    dc = (0, 0, -1, 1)  # 열의 상하좌우

    dq = deque([(0, 0)])  

    row, col = len(maps), len(maps[0])  # 맵의 행과 열 길이
    visited = [[-1] * col for _ in range(row)]  # 방문 기록 배열
    visited[0][0] = 1  # 초기 위치 방문 표시
    
    while dq:
        cr, cc = dq.popleft()  # 현재 위치
        
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]  # 다음 위치
            
            if nr == row - 1 and nc == col - 1:  # 목표 도달
                return visited[cr][cc] + 1
            
            # 맵의 범위를 벗어나거나, 이미 방문했거나, 벽이라면 무시
            if nr < 0 or row <= nr or nc < 0 or col <= nc: 
                continue
            if -1 < visited[nr][nc] or not maps[nr][nc]:
                continue
            
            # 방문 기록시 현재까지 움직인 칸의 개수를 기록
            visited[nr][nc] = visited[cr][cc] + 1
            dq.append((nr, nc))
            
    return -1