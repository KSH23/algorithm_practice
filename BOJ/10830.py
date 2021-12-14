# 10830. 행렬 제곱


def multiply_matrix(matrix1, matrix2):
    ret = [[0] * N for _ in range(N)]
    # 행렬의 곱셈
    for r in range(N):
        for c in range(N):
            for i in range(N):
                ret[r][c] += (matrix1[r][i] * matrix2[i][c]) % 1000
            ret[r][c] %= 1000
    return ret


def matrix_power(power_num):
    # 이미 계산된 값이면 그 값을 불러옴
    if power_num in matrix_dict:
        return matrix_dict[power_num]

    # 거듭 제곱을 분할하여 두 행렬을 곱함
    ret = multiply_matrix(matrix_power(power_num // 2), matrix_power((power_num + 1) // 2))

    matrix_dict[power_num] = ret  # 결과 기록
    return ret


N, B = map(int, input().split())

# 제곱 횟수에 따른 결과 저장할 딕셔너리, 1일때 초기 행렬의 값을 1000으로 나눈 나머지로 바꾼 후 저장
matrix_dict = {1: [list(map(lambda x: x % 1000, map(int, input().split()))) for _ in range(N)]}
result = matrix_power(B)
for row in result:
    print(' '.join(map(str, row)))