# 1535. 평범한 배낭


import sys


N, K = map(int, sys.stdin.readline().split())

# 2차원 배열 계산 시 0행에 0으로 채운 더미 리스트를 넣기 때문에
# 행의 인덱스와 물건의 인덱스를 일치시키기 위해 물건 리스트 앞에도 더미 리스트를 추가
items = [[0, 0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# max_values[i][w]: i번째 물건까지 고려하며 무게 한도가 w일때 최대 가치
values = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for w in range(1, K + 1):
        # 현재 물건을 추가할 수 있는 최대한의 무게(w - items[i][0])의 가치에서 현재 가치를 추가한 값과
        # 현재 물건을 추가하지 않은 최대한의 무게(w)의 가치 중 최댓값을 저장
        if 0 <= w - items[i][0]:
            values[i][w] = max(values[i - 1][w], values[i - 1][w - items[i][0]] + items[i][1])
        else:
            values[i][w] = values[i - 1][w]

print(values[-1][-1])