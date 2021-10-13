# 1717. 집합의 표현


import sys


def find(num):
    if parents[num] == num:  # num이 조상인 경우
        return num

    p_num = find(parents[num])  # 조상 찾기
    parents[num] = p_num  # 조상 저장
    return p_num


def union(num1, num2):
    p_num1 = find(num1)  # num1의 조상
    p_num2 = find(num2)  # num2의 조상
    parents[p_num2] = p_num1


n, m = map(int, input().split())
parents = list(range(n + 1))
for _ in range(m):
    temp = list(map(int, sys.stdin.readline().split()))
    if temp[0]:
        if find(temp[1]) == find(temp[2]):  # 합집합의 경우
            print('YES')
        else:
            print('NO')
    else:
        union(temp[1], temp[2])