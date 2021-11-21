# 11047. 동전 0


import sys


N, target = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]

ans = 0

# 각 동전이 배수 관계를 갖기 때문에 가장 큰 동전 값부터 제거한다
for idx in range(N - 1, -1, -1):
    while coins[idx] <= target:
        ans += target // coins[idx]
        target %= coins[idx]
        continue
    if target == 0:
        break
print(ans)