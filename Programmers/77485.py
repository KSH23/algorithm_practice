# 77485. 행렬 테두리 회전하기


def solution(rows, columns, queries):
    answer = []
    
    # 계산의 편의를 위해 행렬의 상단과 좌측에 하나의 행과 열을 추가
    matrix = [[0] * (columns + 1) for _ in range(rows + 1)]
    
    # 행렬에 숫자를 기입
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            matrix[i][j] = ((i-1) * columns + j)
    
    dr = (0, 1, 0, -1)  # 행의 좌하우상
    dc = (1, 0, -1, 0)  # 열의 좌하우상
    
    for x1, y1, x2, y2 in queries:
        temp = [matrix[x1][y1]]  # 현재 query에서 움직인 숫자 기록
        d = 0  # 방향
        x, y = x1, y1  # 현재 위치
        while d < 4:  # 4 방향을 탐색
            nx, ny = x + dr[d], y + dc[d]  # 다음 위치
            
            # 만약 다음 위치가 범위를 벗어나면 방향 전환
            if nx < x1 or x2 < nx or ny < y1 or y2 < ny:
                d += 1
                continue
            
            # 행렬의 다음 위치에는 이전에 움직인 숫자가 기록되고
            # temp에는 행렬의 다음 위치에 존재하던 숫자를 추가
            matrix[nx][ny], temp = temp[0], [matrix[nx][ny]] + temp
            x, y = nx, ny  # 위치 변경
            
        answer.append(min(temp))  # 정답 갱신
    
    return answer