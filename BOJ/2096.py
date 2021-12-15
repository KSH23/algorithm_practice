# 2096. 내려가기


N = int(input())
first_row = list(map(int, input().split()))  # 첫번째 행

# 인덱스에 도달했을때의 최댓값과 최솟값을 저장하는 배열
# 계산의 편의를 위해 좌측과 우측에 값 추가
max_dp = [0] + first_row + [0]
min_dp = [10 * N] + first_row + [10 * N]

for row in range(1, N):
    next_row = list(map(int, input().split()))  # 다음 행
    cur_max_dp = max_dp[:]  # 현재 최댓값 배열 복사
    cur_min_dp = min_dp[:]  # 현재 최솟값 배열 복사

    # 다음 행의 최댓값과 최솟값 갱신
    for col in range(1, 4):
        max_dp[col] = max(cur_max_dp[col - 1: col + 2]) + next_row[col - 1]
        min_dp[col] = min(cur_min_dp[col - 1: col + 2]) + next_row[col - 1]

print(max(max_dp), end=' ')
print(min(min_dp))