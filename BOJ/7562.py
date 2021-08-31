# 7562. 나이트의 이동


T = int(input())    # 테스트 케이스의 개수
for _ in range(T):
    L = int(input())    # 체스 판의 길이
    CUR = list(map(int, input().split()))    # 현재 좌표
    GOAL = list(map(int, input().split()))    # 목표 좌표

    di = [-2, -1, 1, 2, 2, 1, -1, -2]    # 12시 이후부터 시계방향
    dj = [1, 2, 2, 1, -1, -2, -2, -1]    # 12시 이후부터 시계방향

    Q = [CUR]    # 큐 생성
    visited = [[0] * L for _ in range(L)]    # 최단 경로 저장 리스트
    visited[CUR[0]][CUR[1]] = 1    # 출발 지점을 1로 초기화

    while len(Q) > 0:    # Q가 빌 때 까지 반복
        now = Q.pop(0)    # 현재 좌표
        if now == GOAL:    # 만약 도착 지점에 다다르면 break
            break
        row, col = now[0], now[1]    # 현재 좌표를 row와 col로 나누어 저장

        for k in range(8):
            # 여덟 방향을 검사하여 오류 발생 지점 또는 이미 지나온 곳은 무시
            nr = row + di[k]
            nc = col + dj[k]
            if nr < 0 or nc < 0 or L <= nr or L <= nc:
                continue
            if visited[nr][nc] > 0:
                continue
    
            Q.append([nr, nc])    # 무시되지 않았다면 큐에 저장
            visited[nr][nc] = visited[row][col] + 1    # 경로 또한 저장

    # 최종 답은 1을 뺀 값이지만 만약 visited 값이 0이었다면 음수가 되지 않도록 만든다
    ans = visited[GOAL[0]][GOAL[1]] - 1
    if ans < 0:
        ans = 0
    print(ans)


'''
1) visited[CUR[0]][CUR[1]] = 1 을 해야 하는데 
   visited[CUR[0]][CUR[0]] = 1 으로 적어놓고 1시간 동안 헤매었다
'''