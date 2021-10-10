# 2961. 도영이가 만든 맛있는 음식


def cook(ingredients):
    s, b = 1, 0
    for ingredient in ingredients:
        s *= ingredient[0]
        b += ingredient[1]

    return abs(s - b)


N = int(input())
flavor_list = [list(map(int, input().split())) for _ in range(N)]

ans = 1000000000
for i in range(1, 1 << N):
    ingredients_list = []
    for j in range(N + 1):
        if i & (1 << j):
            ingredients_list.append(flavor_list[j])
    cooK_result = cook(ingredients_list)
    if cooK_result < ans:
        ans = cooK_result
print(ans)