# 43105. 정수 삼각형


def solution(triangle):
    # triangle[i][j]까지 도달하였을 때 가질 수 있는 최댓값을 리스트에 기록
    for row in range(1, len(triangle)):
        # 삼각형의 최좌측과 최우측은 한 가지 경우의 수만을 가짐
        triangle[row][0] += triangle[row - 1][0]
        triangle[row][-1] += triangle[row - 1][-1]

        # 남은 숫자들은 두 가지 경우의 수를 가지며 이에 대해 최댓값을 기록
        for col in range(1, len(triangle[row]) - 1):
            triangle[row][col] += max(triangle[row - 1][col - 1: col + 1])

    return max(triangle[-1])
