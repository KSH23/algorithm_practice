# 1992. 쿼드트리


import sys


def check(start_row, start_col, size):
    # MAP을 탐색하며 모두 같은 수를 갖지 않았다면 False,
    # 모두 같은 수를 가지고 있다면 True 반환
    for row in range(start_row, start_row + size):
        for col in range(start_col, start_col + size):
            if MAP[start_row][start_col] != MAP[row][col]:
                return False
    return True


def quad_tree(first_r, first_c, size):
    ret = '('
    for start_r in range(first_r, first_r + size * 2, size):
        for start_c in range(first_c, first_c + size * 2, size):
            if N <= start_r or N <= start_c:
                continue  # 범위 밖

            # 쪼개진 영상이 같은 수를 갖는 경우 숫자를 추가
            if check(start_r, start_c, size):
                ret += str(MAP[start_r][start_c])
            else:  # 모두 일치하는 수를 갖지 않는 경우 다시 사등분
                ret += quad_tree(start_r, start_c, size // 2)
    ret += ')'
    return ret


N = int(sys.stdin.readline())
MAP = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

if check(0, 0, N):  # 주어진 영상이 모두 동일한 숫자를 갖는 경우
    print(MAP[0][0])
else:
    print(quad_tree(0, 0, N // 2))