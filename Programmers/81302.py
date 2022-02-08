# 81302. 거리두기 확인하기


from collections import deque


def bfs(place, row, col):
    dr = (-1, 1, 0, 0)  # 행 상하좌우
    dc = (0, 0, -1, 1)  # 열 상하좌우

    # 방문 기록 배열에 초기 위치 방문 표시
    visited = [[False] * 5 for _ in range(5)]
    visited[row][col] = True

    dq = deque([(row, col)])  # 초기 위치 설정

    # 맨해튼 거리가 2 이하인 영역은 bfs의 깊이가 2인 경우
    for _ in range(2):
        for _ in range(len(dq)):
            cr, cc = dq.popleft()  # 현재 위치

            for d in range(4):
                nr, nc = cr + dr[d], cc + dc[d]  # 다음 위치

                # 영역을 벗어나거나, 방문했거나, 파티션인 경우 무시
                if nr < 0 or 5 <= nr or nc < 0 or 5 <= nc:
                    continue
                if visited[nr][nc] or place[nr][nc] == "X":
                    continue

                # 응시자를 만난 경우 거리두기 실패
                if place[nr][nc] == "P":
                    return 0

                visited[nr][nc] = True  # 다음 위치 방문 표시
                dq.append((nr, nc))  # 다음 위치 추가

    # 거리두기 성공
    return 1


def solution(places):
    answer = []
    for place in places:
        flag = 1  # 거리두기 여부
        for r in range(5):
            if not flag:  # 거리두기 실패
                break
            for c in range(5):
                if place[r][c] == "P":
                    # bfs 함수의 결과가 0인 경우 거리두기 실패
                    if not bfs(place, r, c):
                        flag = 0
                        break
        answer.append(flag)

    return answer