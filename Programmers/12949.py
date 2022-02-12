# 12949. 행렬의 곱셈


def solution(arr1, arr2):
    row, col = len(arr1), len(arr2[0])  # 행렬의 크기
    answer = [[0] * col for _ in range(row)]  # 행렬 생성

    # 행렬의 각 칸에 해당하는 값을 계산하여 기록
    for r in range(row):
        for c in range(col):
            answer[r][c] = sum(arr1[r][i] * arr2[i][c] for i in range(len(arr2)))

    return answer