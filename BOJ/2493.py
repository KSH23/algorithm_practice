# 2493. 탑


import sys
from collections import deque


N = int(input())
towers = list(map(int, sys.stdin.readline().split()))
stack = deque()
stack.append([towers[-1], len(towers)])
ans = [0] * len(towers)  # 최종 정답

for idx in range(len(towers) - 2, -1, -1):
    # 탑을 우측에서 시작해 검사하며 현재 idx 탑보다 더 낮은 탑에 대하여 반복
    while stack and towers[idx] > stack[-1][0]:
        ans[stack[-1][1] - 1] = idx + 1  # 수신하는 탑 기록
        stack.pop()
    stack.append([towers[idx], idx + 1])

for item in ans:
    print(item, end=' ')
print()