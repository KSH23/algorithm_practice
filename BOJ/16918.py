# 16918. 봄버맨


def find_bomb(board):  # 2차원 리스트를 받음
    bombs = []
    for r in range(R):
        for c in range(C):
            if board[r][c] == 'O':
                bombs.append([r, c])
    return bombs  # 폭탄의 좌표를 담은 리스트 반환


def boom(bomb_coord):  # 폭탄의 좌표가 담긴 리스트를 받음
    board = [['O'] * C for _ in range(R)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for coord in bomb_coord:
        r, c = coord[0], coord[1]
        board[r][c] = '.'
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nc < 0 or R <= nr or C <= nc:
                continue
            if board[nr][nc] == '.':
                continue
            board[nr][nc] = '.'

    return board  # 폭탄이 터진 이후의 2차원 리스트를 반환


R, C, T = map(int, input().split())
MAP = [list(input()) for _ in range(R)]

if T == 1:  # 아무것도 하지 않은 경우
    for row in range(R):
        print(''.join(MAP[row]))
else:
    T = T % 4  # 1초를 넘기면 이후는 반복
    if T == 2 or T == 0:
        for _ in range(R):
            print('O' * C)
    elif T == 3:  # (4n - 3)초일 경우
        third = boom(find_bomb(MAP))
        for row in range(R):
            print(''.join(third[row]))
    else:  # (4n + 1)초일 경우
        third = boom(find_bomb(MAP))
        fifth = boom(find_bomb(third))
        for row in range(R):
            print(''.join(fifth[row]))