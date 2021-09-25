# 2798. 블랙잭


N, M = map(int, input().split())
cards = list(map(int, input().split()))
ans = 0
for num1 in cards:
    for num2 in cards:
        if num2 == num1:
            continue
        for num3 in cards:
            if num3 == num2 or num3 == num1:
                continue
            my_num = num1 + num2 + num3
            if ans < my_num <= M:
                ans = my_num

print(ans)