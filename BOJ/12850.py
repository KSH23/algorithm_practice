# 12850. 본대 산책2


def multiply_matrix(matrix1, matrix2):
    result = []  # 두 행렬의 곱의 결과 저장 리스트

    for row1 in range(len(matrix1)):
        temp = []  # 결과 행렬의 새로운 행
        for col2 in range(len(matrix1[0])):
            temp_value = 0  # 결과 행렬의 새로운 열
            for col1 in range(len(matrix2[0])):
                temp_value += matrix1[row1][col1] * matrix2[col1][col2]
            temp.append(temp_value % 1000000007)
        result.append(temp)
    return result


def power_matrix(power):
    # 만약 행렬의 power 제곱을 이미 했었다면 그 결과 반환
    if power in power_memo:
        return power_memo[power]

    # power 제곱을 두 개의 제곱 연산으로 분할
    mat1 = power_matrix(power // 2)
    mat2 = power_matrix((power + 1) // 2)

    ret = multiply_matrix(mat1, mat2)
    power_memo[power] = ret  # 연산 결과를 기록
    return ret


D = int(input())
MAP = [
    [0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 0]
]

power_memo = {1: MAP}  # key: 제곱하는 횟수, value: 그 결과
print(power_matrix(D)[0][0])