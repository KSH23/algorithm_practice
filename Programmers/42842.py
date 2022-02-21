# 42842. 카펫


def solution(brown, yellow):
    # brown = (2 * row) + (2 * col) - 4
    # yellow = (row - 2) * (col - 2)
    # 따라서 col = (brown / 2) + 2 - row이며
    # 다음과 같은 일차 방정식을 구할 수 있음
    # yellow = (row - 2) * (brown / 2 - row)
    for row in range(3, brown // 2):
        if (row - 2) * (brown // 2 - row) == yellow:
            return [max(row, brown // 2 + 2 - row), min(row, brown // 2 + 2 - row)]