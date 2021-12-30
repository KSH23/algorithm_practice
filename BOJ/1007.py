# 1007. 벡터 매칭


import sys


def make_points_sequence(cur_idx, sequence):
    global ans

    if len(sequence) == N // 2:
        # (N // 2) 크기의 수열이 만들어지면 수열에 속한
        # 모든 점의 좌표 값을 더한 뒤 빼면 최종 벡터
        result_x = total_x
        result_y = total_y
        for idx in sequence:
            result_x -= 2 * points[idx][0]
            result_y -= 2 * points[idx][1]
    
        # 최소 백터의 크기 갱신
        ans = min(ans, (result_x ** 2 + result_y ** 2) ** 0.5)
        return

    # 중복되지 않는 순열 생성
    for idx in range(cur_idx + 1, N):
        if used_points[idx]:
            continue
        used_points[idx] = True
        make_points_sequence(idx, sequence + [idx])
        used_points[idx] = False


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    points = []  # 점의 좌표 저장
    total_x = total_y = 0  # 모든 점의 x좌표 총 합, y좌표 총 합
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        total_x += x
        total_y += y
        points.append((x, y))
        
    used_points = [False] * N  # 사용한 점 기록
    ans = 400000000  # 최종 정답
    make_points_sequence(-1, [])

    print(ans)