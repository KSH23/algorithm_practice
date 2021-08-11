# 10157. 자리배정


# 알고리즘 수업에서 배운 델타 검색 방식을 그대로 이용
# 하지만 시간이 매우 오래걸림
def your_seat(c, r, k):
    # 문제의 그림을 우측으로 90도 회전한 것을 기준으로 삼음
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    d = 0    # 방향 전환용 변수
    i, j = 0, -1    # 초기 위치
    cnt = 0    # 좌석 번호용 변수
    result = [[0] * r for _ in range(c)]    # rXc 크기의 좌석 생성

    if k > c*r:    # 만약 k가 좌석 갯수보다 크다면 0 return
        return [0]    # 이후 출력을 위해 리스트 형태로 반환

    while cnt <= k:    # cnt가 k에 도달할 때까지 반복
        # 만약 현재 위치가 경계를 넘는다던가 0이 아닌 숫자를 만난다면 방향 전환
        if c <= i + di[d] or r <= j + dj[d] or i + di[d] < 0 or j + dj[d] < 0:
            d = (d + 1) % 4
        elif result[i + di[d]][j + dj[d]] != 0:
            d = (d + 1) % 4
        else:    # 위 두 조건을 피했다면
            cnt += 1    # 현재 좌석 번호
            i, j = i + di[d], j + dj[d]    # 해당 위치로 이동
            result[i][j] = 1    # 좌석 번호 추가

        if cnt == k:    # 현재 좌석 번호가 k라면 return
            return [i + 1, j + 1]


C, R = map(int, input().split())
K = int(input())
print(' '.join(map(str, your_seat(C, R, K))))