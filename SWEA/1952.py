# 1952. 수영장


def dfs(start, price):
    global min_price

    if start > 12 and 0 < price < min_price:
        min_price = price
        return

    if start > 12:    # 13월부터는 중단
        return

    if min_price < price:    # 중간에 최솟값보다 비싸지면 중단
        return

    if plan_list[start] == 0:
        dfs(start + 1, price)

    if start <= 12 and plan_list[start] > 0:
        dfs(start + 1, price + price_list[0] * plan_list[start])  # 1일 이용권
        dfs(start + 1, price + price_list[1])  # 1달 이용권
        dfs(start + 3, price + price_list[2])  # 3달 이용권


T = int(input())
for tc in range(1, T+1):
    price_list = list(map(int, input().split()))
    plan_list = [0] + list(map(int, input().split()))
    min_price = price_list[-1]    # 1년 이용권으로 최솟값 초기화
    for i in range(1, 13):
        if plan_list[i]:
            dfs(i, 0)
            break
    print(f'#{tc} {min_price}')