# 68645. 삼각 달팽이


def make_list(n):
    snail_list = [[0] * n for _ in range(n)]

    dr = (1, 0, -1)  # 행의 하, 우, 좌상
    dc = (0, 1, -1)  # 열의 하, 우, 좌상

    cur_row, cur_col = -1, 0  # 초기값 설정
    num = 1  # 리스트에 적힐 숫자
    step = n  # 그려질 삼각형의 크기
    while 0 < step:
        for d in range(3):  # 세 방향
            for _ in range(step - d):
                cur_row += dr[d]
                cur_col += dc[d]

                # 이미 숫자가 기록된 경우 삼각 달팽이 완성
                if snail_list[cur_row][cur_col]:
                    return snail_list
                snail_list[cur_row][cur_col] = num
                num += 1

        step -= 3

    return snail_list


def solution(n):
    answer = []

    snail_list = make_list(n)  # 생성된 삼각 달팽이 리스트

    for row in range(n):
        for col in range(n):
            if snail_list[row][col]:
                answer.append(snail_list[row][col])

    return answer
