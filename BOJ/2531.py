# 2531.회전 초밥


import sys


N, d, k, c = map(int, sys.stdin.readline().split())
sushi_table = [int(sys.stdin.readline()) for _ in range(N)]

ans = 0  # 최종 정답
end = N - 1  # 끝나는 지점 인덱스
start = end - k + 1  # 시작 지점 인덱스, 이후 음수가 되어 테이블을 원형으로 탐색

# 모든 경우를 검사하기 전 첫 기준 초밥 종류 체크 리스트를 만듦
sushi_check = [0] * (d + 1)  # 초밥 종류 체크 리스트
sushi_cnt = 0  # 초밥 가짓수 개수
for idx in range(end, start - 1, -1):  # 초밥 테이블을 역순으로 검사
    if sushi_check[sushi_table[idx]] == 0:  # 만약 현재 초밥이 체크되어있지 않다면
        sushi_cnt += 1  # 초밥 가짓수 증가
    sushi_check[sushi_table[idx]] += 1  # 초밥 체크

ans = 0  # 최종 정답

while end >= 0:
    sushi_check[sushi_table[end]] -= 1
    # 만약 현재 end 위치의 초밥을 체크 해제하였을 때 값이 0이 된다면
    if sushi_check[sushi_table[end]] == 0:
        sushi_cnt -= 1  # 가짓수를 줄이고
    end -= 1  # 한 칸 왼쪽으로 전진

    start -= 1  # 한 칸 왼쪽으로 전진
    # 만약 현재 start 위치의 초밥이 체크되어있지 않다면
    if sushi_check[sushi_table[start]] == 0:
        sushi_cnt += 1  # 가짓수를 늘리고
    sushi_check[sushi_table[start]] += 1  # 초밥 체크

    if sushi_check[c] == 0:  # 만약 쿠폰 초밥이 포함되어있지 않다면
        if sushi_cnt + 1 > ans:  # 쿠폰 포함 초밥 가짓수가 최댓값이 된다면
            ans = sushi_cnt + 1  # 정답 갱신
    else:  # 만약 쿠폰 초밥이 이미 포함되어 있다면
        if sushi_cnt > ans:  # 만약 현재 초밥 가짓수가 최댓값이 된다면
            ans = sushi_cnt  # 정답 갱신

print(ans)