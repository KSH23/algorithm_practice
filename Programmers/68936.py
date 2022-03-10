# 68936. 쿼드압축 후 개수 세기


def is_same_num(arr, row, col, size):
    """
    arr에서 row, col을 시작점으로 잡았을 때 size 크기만큼의
    정사각형이 모두 같은 수로 채워졌는지 판단하는 함수
    """
    for r in range(row, row + size):
        for c in range(col, col + size):
            if arr[r][c] != arr[row][col]:
                return False
    return True


def solution(arr):
    answer = [0, 0]

    # 각 정사각형의 좌측 상단 꼭지점과 크기를 저장하는 리스트
    start_points = [(0, 0, len(arr))]  # (row, col, size)
    
    while start_points:
        row, col, size = start_points.pop()
        
        if is_same_num(arr, row, col, size):
            answer[arr[row][col]] += 1

        else:  # 정사각형이 같은 수로 채워지지 않은 경우
            size //= 2
            start_points.append((row, col, size))
            start_points.append((row + size, col, size))
            start_points.append((row, col + size, size))
            start_points.append((row + size, col + size, size))
    
    return answer