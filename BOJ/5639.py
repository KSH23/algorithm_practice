# 5639. 이진 검색 트리


import sys


sys.setrecursionlimit(100000)


def dfs(start, end):
    if start > end:
        return

    right = end
    while data[right] > data[start]:
        right -= 1

    dfs(start + 1, right)
    dfs(right + 1, end)
    print(data[start])


data = list(map(int, sys.stdin.read().split()))
dfs(0, len(data) - 1)