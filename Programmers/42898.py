# 42898. 등굣길


def solution(m, n, puddles):
    route = [[0] * (n + 1) for _ in range(m + 1)]  # 격자 지도
    route[0][1] = 1  # route[1][1]에 1이 기록될 수 있도록 임의로 추가한 값
    for row, col in puddles:  # 웅덩이는 -1을 기록
        route[row][col] = -1

    for row in range(1, m + 1):
        for col in range(1, n + 1):
            if route[row][col] == -1:  # 웅덩이는 무시
                continue

            # 현재 좌표까지 최단거리로 도달할 수 있는 방법은 상 또는 좌에서 오는 길
            # 웅덩이의 경우는 0으로 계산되도록 max() 함수 이용
            route[row][col] = max(0, route[row - 1][col]) + max(0, route[row][col - 1])

    return route[m][n] % 1000000007
