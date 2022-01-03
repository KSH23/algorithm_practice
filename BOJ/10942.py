# 10942. 팰린드롬?


import sys


sys.setrecursionlimit(100000)


def check_palindrome(s, e):
    # 이미 팰린드롬인지 계산된 경우
    if is_palindrome[s][e] != -1:
        return is_palindrome[s][e]

    # 숫자 하나는 무조건 팰린드롬
    if s == e:
        return 1

    # 숫자 두 개의 경우, 두 숫자가 같은 경우에만 팰린드롬
    if e - s == 1 and num_list[s] == num_list[e]:
        return 1

    # 숫자 세 개 이상의 경우
    # 양 끝의 숫자가 같으면서 그 사이의 수가 팰린드롬인 경우에만 팰린드롬
    if num_list[s] == num_list[e] and check_palindrome(s + 1, e - 1):
        return 1

    return 0


N = int(sys.stdin.readline())
num_list = [0] + list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

# is_palindrome[s][e] = s 번째에서 e 번째 까지의 수가 팰린드롬인가?
# 그렇다면 1, 아니라면 0, 결정되지 않았다면 -1 기록
is_palindrome = [[-1] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    # 팰린드롬인지 아직 결정되지 않은 경우 함수 실행
    if is_palindrome[S][E] == -1:
        is_palindrome[S][E] = check_palindrome(S, E)
    print(is_palindrome[S][E])