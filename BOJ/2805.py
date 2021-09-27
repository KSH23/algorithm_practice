# 2805. 나무 자르기


def cut_trees(height):    # 자른 나무 개수를 구하는 함수
    wood = 0
    for tree in trees:
        if tree > height:
            wood += tree - height
    return wood


N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
ans = 0    # 최종 답

while start <= end:    # 이분탐색 진행
    mid = (start + end) // 2
    my_wood = cut_trees(mid)
    if my_wood < M:
        end = mid - 1
    elif my_wood >= M:
        start = mid + 1
        if ans < mid:
            ans = mid    # 최댓값 갱신

print(ans)