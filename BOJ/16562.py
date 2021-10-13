# 16562. 친구비


import sys


def find(x):
    if parents[x] == x:  # x가 x의 조상인 경우
        return x

    p_x = find(parents[x])  # x의 조상
    parents[x] = p_x  # 조상 정보 갱신
    return p_x


def union(x, y):
    p_x, p_y = find(x), find(y)  # 조상 찾기
    p_x_cost, p_y_cost = cost_list[p_x], cost_list[p_y]  # 각 조상의 비용

    # 더 값 싼 조상을 대표자로 만들고 가격 갱신
    if p_x_cost <= p_y_cost:
        parents[p_y] = p_x
        group_cost_list[p_y] = 0
    elif p_x_cost > p_y_cost:
        parents[p_x] = p_y
        group_cost_list[p_x] = 0


N, M, k = map(int, input().split())
parents = list(range(N + 1))
cost_list = [0] + list(map(int, sys.stdin.readline().split()))
group_cost_list = cost_list[:]  # cost_list 복사
for _ in range(M):
    temp = list(map(int, sys.stdin.readline().split()))
    union(temp[0], temp[1])  # 친구 관계 갱신

total_cost = sum(group_cost_list)
if total_cost <= k:  # 돈이 충분한 경우
    print(sum(group_cost_list))
else:  # 돈이 부족한 경우
    print('Oh no')