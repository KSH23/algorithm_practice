# 5209. 최소 생산 비용


def total_cost(cost, product):
    global ans

    if ans < cost:  # 이미 최솟값을 넘긴 경우
        return

    if product == N:  # 제품을 모두 완성한 경우
        if cost < ans:  
            ans = cost  # 최솟값 갱신
        return

    for plant in range(N):
        if plant_check[plant]:  # 이미 이용한 공장은 넘어감
            continue
        plant_check[plant] = 1
        total_cost(cost + COST_TABLE[product][plant], product + 1)
        plant_check[plant] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    COST_TABLE = [list(map(int, input().split())) for _ in range(N)]
    plant_check = [0] * N  # 이용한 공장 표시
    ans = 99 * N * N  # 최종 정답
    total_cost(0, 0)
    print(f'#{tc} {ans}')