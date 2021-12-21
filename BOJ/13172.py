# 13172. Σ


import sys


def power(base, num):
    if num == 0:
        return 1
    elif num == 1:
        return base

    if num % 2:
        return (((power(base, num // 2) % MOD) ** 2) * base) % MOD
    else:
        return ((power(base, num // 2) % MOD) ** 2) % MOD


M = int(sys.stdin.readline())
MOD = 1000000007
total = 0  # 모든 주사위를 한 번씩 던졌을 때 나온 숫자들의 합의 기댓값
for _ in range(M):
    N, S = map(int, sys.stdin.readline().split())
    # b^(X - 2) = b^(-1) (mod X) 이므로 b^(X - 2) % X = b^(-1)이다
    result = power(N, MOD - 2)  # 따라서 b^(X - 2) % X 값을 구한 뒤 S를 곱한 후
    total += (result * S) % MOD  # (mod X) 연산을 한 결과가 답이다
print(total % MOD)