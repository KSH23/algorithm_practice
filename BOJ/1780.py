# 1780. 종이의 개수


import sys


def check_paper(row, col, size):
    # 종이에 적힌 수가 같으면 True, 아니면 False 반환
    for r in range(row, row + size):
        for c in range(col, col + size):
            if MAP[row][col] != MAP[r][c]:
                return False
    return True


def cut_paper(start_row, start_col, size):
    for start_r in range(start_row, start_row + size * 3, size):
        for start_c in range(start_col, start_col + size * 3, size):
            # 범위를 벗어나는 인덱스는 무시
            if N <= start_r or N <= start_c:
                continue

            # 만약 모두 같은 수가 적힌 종이라면 해당 갯수를 증가시키고
            if check_paper(start_r, start_c, size):
                cnt_list[MAP[start_r][start_c] + 1] += 1
            else:  # 그렇지 않다면 크기를 1/3으로 줄인 후 다시 함수 실행
                cut_paper(start_r, start_c, size // 3)


N = int(sys.stdin.readline())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cnt_list = [0, 0, 0]  # [인덱스 -1] 숫자의 갯수를 담는 리스트

cut_paper(0, 0, N)

for cnt in cnt_list:
    print(cnt)