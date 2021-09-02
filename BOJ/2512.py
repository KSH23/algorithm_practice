# 2512. 예산


N = int(input())    # 지방의 수
budget = list(map(int, input().split()))    # 예산 리스트
total_budget = int(input())    # 총 예산

budget.sort()    # 이분탐색을 사용하기 위하여 리스트를 오름차순 정렬
start = 0
end = budget[-1]
ans = 0    # 최종 상한액 변수

'''
1. start와 end를 budget[0]과  budget[-1]으로, 
   mid를 budget[start]와 budget[end]의 평균으로 설정한다
2. mid가 상한액일때 예산의 총 합을 구한다
3. 만약 예산의 총 합이 총 예산보다 적으며 기존의 ans보다 크다면 ans에 저장하고 start는 mid가 된다
4. 총 예산보다 크다면 end는 mid가 된다
5. 이를 start가 end보다 크거나 같아질 때 까지 반복한다
'''

while start <= end:
    mid = (start + end) // 2

    needed_budget = 0    # 필요한 예산
    for b in budget:
        if b <= mid:    # 상한액보다 적은 예산은 그냥 더하고
            needed_budget += b
        else:    # 상한액보다 큰 예산은 상한액으로 더함
            needed_budget += mid

    # 기존에 저장된 상한액과 비교하고 필요한 예산과 총 예산을 비교하여 탐색을 진행
    if ans < mid and needed_budget <= total_budget:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)


'''
1) 처음 start를 budget[0]으로 설정하였었는데 
   이렇게 하면 최소 예산보다 적은 상한액을 배정할 수 없어 수정하였다
'''
