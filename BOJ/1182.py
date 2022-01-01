# 1182. 부분수열의 합 


import sys


def subsequence_sum(cur_idx, size, total_sum):
    global ans

    # 크기가 양수이며 총 합이 S인 경우 답 증가
    if total_sum == S and size:
        ans += 1
    
    # 범위 밖 도달
    if cur_idx == N:
        return
    
    # 부분 수열 생성
    for idx in range(cur_idx + 1, N):
        subsequence_sum(idx, size + 1, total_sum + num_list[idx])


N, S = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
ans = 0  # 최종 정답
subsequence_sum(-1, 0, 0)
print(ans)