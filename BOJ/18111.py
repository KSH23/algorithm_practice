# 18111. 마인크래프트


import sys

N, M, B = map(int, sys.stdin.readline().split())

# 주어진 땅이 2차원 리스트로 저장되야할 이유가 없어 1차원 리스트로 저장
lands = []
for _ in range(N):
    lands += list(map(int, sys.stdin.readline().split()))

lands.sort(reverse=True)  # 오름차순 정렬
max_height = lands[0]  # 최고 높이
min_height = lands[-1]  # 최저 높이

ans_s, ans_h = 250000000, 0  # 최종 시간과 높이

# 최저 높이부터 최고 높이까지 기준 높이를 설정하여 검사
for height in range(max_height, min_height - 1, -1):
    blocks = B  # 쓸 수 있는 블록 수
    sec = 0  # 소요되는 시간
    for land in lands:  # 모든 땅에 대해 탐색
        if land < height:  # 기준 높이보다 낮은 경우
            if height - land <= blocks:
                sec += height - land
                blocks -= height - land
            else:  # 블록이 부족하다면 중단
                break

        elif land > height:  # 기준 높이보다 높은 경우
            sec += (land - height) * 2
            blocks += land - height
    else:  # 모든 땅을 검사했다면 정답 갱신
        if -1 < sec < ans_s:
            ans_s = sec
            ans_h = height
        elif sec == ans_s:
            ans_h = max(height, ans_h)

print(ans_s, ans_h)