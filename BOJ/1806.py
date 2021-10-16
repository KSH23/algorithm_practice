# 1806. 부분합


import sys


N, S = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
right = -1  # 우측 포인터
current_sum = 0  # 부분합
ans = N + 1  # 가장 짧은 길이 == 최종 정답

for left in range(N):  # 좌측 포인터를 0부터 N-1까지 돌림
    # 현재 부분합이 S보다 크게 만들도록 시도
    while current_sum < S and right < N - 1:
        right += 1
        current_sum += num_list[right]

    if S <= current_sum:  # 만들어진 부분합이 S 이상인 경우
        length = right - left + 1
        if length < ans:
            ans = length

    current_sum -= num_list[left]

if ans == N + 1:
    print(0)
else:
    print(ans)