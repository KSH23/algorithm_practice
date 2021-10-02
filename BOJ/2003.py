# 2003. 수들의 합 2


N, M = map(int, input().split())
num_list = list(map(int, input().split()))
ans = 0  # 최종 정답
start = 0  # 수들의 시작 지점
end = 0  # 수들의 끝나는 지점
list_sum = num_list[0]  # 수들의 합

while True:
    if list_sum < M:  # 만약 수들의 합이 M보다 작다면
        end += 1  # 끝나는 지점을 우측으로 이동
        if end >= N:  # 리스트 경계 확인
            break
        list_sum += num_list[end]
    elif M < list_sum:  # 만약 수들의 합이 M보다 크다면
        list_sum -= num_list[start]  # 시작 지점을 빼고
        start += 1  # 시작 지점을 우측으로 이동
        if start >= N:  # 리스트 경계 확인
            break
        if start > end:  # 시작지점이 앞서나가면
            end += 1  # 끝나는 지점을 하나 늘림
            list_sum += num_list[end]
    else:  # 수들의 합이 M을 만족시키는 경우
        ans += 1  # 최종 정답을 증가시키고
        end += 1  # 끝나는 지점을 우측으로 이동
        if end >= N:  # 리스트 경계 확인
            break
        list_sum += num_list[end]

print(ans)