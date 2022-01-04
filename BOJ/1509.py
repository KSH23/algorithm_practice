# 1509. 팰린드롬 분할


import sys


sys.setrecursionlimit(100000)


def check_palindrome(s, e):
    # 이미 팰린드롬인지 계산된 경우
    if is_palindrome[s][e] != -1:
        return is_palindrome[s][e]

    # 문자 하나는 무조건 팰린드롬
    if s == e:
        is_palindrome[s][e] = 1
        return 1

    # 문자 두 개의 경우, 두 문자가 같은 경우에만 팰린드롬
    if e - s == 1 and string[s] == string[e]:
        is_palindrome[s][e] = 1
        return 1

    # 문자 세 개 이상의 경우
    # 양 끝의 문자가 같으면서 그 사이의 문자가 팰린드롬인 경우에만 팰린드롬
    if string[s] == string[e] and check_palindrome(s + 1, e - 1):
        is_palindrome[s][e] = 1
        return 1

    is_palindrome[s][e] = 0
    return 0


string = sys.stdin.readline().rstrip()
L = len(string)  # 문자열의 길이

# is_palindrome[s][e] = s 번째에서 e 번째 까지의 문자열이 팰린드롬인가?
# 그렇다면 1, 아니라면 0, 결정되지 않았다면 -1 기록
is_palindrome = [[-1] * L for _ in range(L)]

dp = [0] * L  # i 번째 까지의 문자열에서 분할의 개수의 최솟값 저장

for idx in range(L):
    # idx 번째 까지의 문자열이 팰린드롬인 경우
    if check_palindrome(0, idx) == 1:
        dp[idx] = 1
        continue

    # idx 번째 까지의 문자열을 두 부분으로 분할하여 계산
    temp = L + 1
    for start_idx in range(1, idx + 1):
        # start_idx 번째에서 idx 번째 까지의 문자열이 팰린드롬인 경우
        if check_palindrome(start_idx, idx) == 1:
            temp = min(dp[start_idx - 1] + 1, temp)
    dp[idx] = temp

print(dp[L - 1])