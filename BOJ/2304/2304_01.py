# 2304. 창고 다각형


import sys


def warehouse(start, end, direction):
    curr_column = ()  # 현재 최고 높이 기둥 정보
    area = 0  # 창고 면적
    for idx in range(start, end, direction):
        # 최고 높이 기둥을 넘어서면 중지
        if columns[idx][0] * direction > max_l * direction:
            return area

        if not curr_column:  # 저장된 기둥 정보가 없는 경우 초기 정보 저장
            curr_column = columns[idx]

        # 더 높은 기둥을 만난 경우 면적과 현재 최고 높이 기둥 갱신
        elif curr_column[1] <= columns[idx][1]:  
            area += (columns[idx][0] - curr_column[0]) * curr_column[1] * direction
            curr_column = columns[idx]
    return area


N = int(sys.stdin.readline())

# 기둥의 왼쪽 면의 위치, 높이를 튜플로 리스트에 저장
columns = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
columns.sort()  # 왼쪽 면의 위치를 기준으로 정렬

# 최고 높이 기둥의 위치를 구해 이를 기준으로 좌측, 우측 창고를 따로 계산
max_l, max_height = max(columns, key=lambda x: x[1])

ans = warehouse(0, N, 1)  # 최고 높이 기둥의 좌축
ans += warehouse(N - 1, -1, -1)  # 최고 높이 기둥의 우측

print(ans + max_height)
