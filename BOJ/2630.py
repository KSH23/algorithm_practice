# 2630. 색종이 만들기


def paper(start_coord, size):
    row = start_coord[0]  # 시작 지점의 행
    col = start_coord[1]  # 시작 지점이 열
    for i in range(row, row + size):
        for j in range(col, col + size):
            if MAP[i][j] != MAP[row][col]:
                # 다른 색이 나온 경우 사등분 하여 같은 작업 반복하여 진행
                paper((row, col), size // 2)
                paper((row, col + size // 2), size // 2)
                paper((row + size // 2, col), size // 2)
                paper((row + size // 2, col + size // 2), size // 2)
                return

    color[MAP[row][col]] += 1  # 모든 for loop 후 색종이 개수 갱신


N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
color = [0, 0]  # 흰색 종이 개수, 파란색 종이 개수를 저장하는 리스트
paper((0, 0), N)
print(color[0])
print(color[1])