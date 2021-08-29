# 17616. 등수 찾기


import sys
from collections import deque


N, M, X = map(int, input().split())
better = [[] for _ in range(N+1)]
worse = [[] for _ in range(N+1)]
for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    better[B] += [A]
    worse[A] += [B]

# print(better, worse)

check = [0] * (N+1)

good_Q = deque()
good_Q.append(X)
check[X] = 1
good_cnt = 0
while len(good_Q) > 0:
    now = good_Q.popleft()

    for item in better[now]:
        if check[item] == 1:
            continue
        good_Q.append(item)
        check[item] = 1

    good_cnt += 1

print(good_cnt, end=' ')


check = [0] * (N+1)

bad_Q = deque()
bad_Q.append(X)
check[X] = 1
bad_cnt = 0
while len(bad_Q) > 0:
    now = bad_Q.popleft()

    for item in worse[now]:
        if check[item] == 1:
            continue
        bad_Q.append(item)
        check[item] = 1

    bad_cnt += 1

print(N - bad_cnt + 1)