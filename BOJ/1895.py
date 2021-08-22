# 1895. 필터


def find_median(row, col, matrix):
    # row, col, 행렬을 받으면 해당 row와 col을 기준으로
    # 3x3의 크기로 검사한 후 중앙값을 반환하는 함수
    filter_list = []
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            filter_list += [matrix[i][j]]
    filter_list.sort()

    return filter_list[4]


R, C = map(int, input().split())
I = [list(map(int, input().split())) for _ in range(R)]
T = int(input())

J = [[0] * (C-2) for _ in range(R-2)]    # 필터링된 이미지

for i in range(R-2):
    for j in range(C-2):
        # 중앙값을 찾는 함수를 이용하여 필터링된 이미지 생성
        J[i][j] = find_median(i, j, I)

ans = 0
for i in range(R-2):    # J에서 T보다 크거나 같은 값을 찾아 count
    for j in range(C-2):
        if J[i][j] >= T:
            ans += 1
print(ans)