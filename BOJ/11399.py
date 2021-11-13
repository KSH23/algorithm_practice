# 11399. ATM


import sys


N = int(sys.stdin.readline())
people = list(map(int, sys.stdin.readline().split()))
people.sort()  # 줄이 오름차순 정렬되었을 때가 시간이 최소

total = 0  # 총 걸린 시간
for index, person in enumerate(people):
    total += person * (N - index)

print(total)