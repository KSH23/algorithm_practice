# 60059. 자물쇠와 열쇠


def solution(key, lock):
    m, n = len(key), len(lock)

    # 열쇠의 위치를 각 방향마다 나누어 저장
    key_location = [[], [], [], []]
    for row in range(m):
        for col in range(m):
            if key[row][col]:
                key_location[0].append((row, col))
                key_location[1].append((col, m - 1 - row))
                key_location[2].append((m - 1 - row, m - 1 - col))
                key_location[3].append((m - 1 - col, row))

    lock_location = set()  # 자물쇠의 위치를 저장
    for row in range(n):
        for col in range(n):
            if not lock[row][col]:
                lock_location.add((row, col))

    for row in range(n + m):
        for col in range(n + m):
            for direction in range(4):
                temp_lock = lock_location.copy()
                for r, c in key_location[direction]:
                    # 현재 방향의 열쇠를 (0, 0)에서 (row, col)만큼 이동한 결과
                    shift_r = r - (m - 1) + row
                    shift_c = c - (m - 1) + col

                    # 열쇠가 자물쇠 범위를 벗어나는 경우 무시
                    if shift_r < 0 or n <= shift_r or shift_c < 0 or n <= shift_c:
                        continue

                    # 열쇠가 홈이 아닌 곳에 있는 경우
                    if (shift_r, shift_c) not in lock_location:
                        break

                    temp_lock.discard((shift_r, shift_c))

                if len(temp_lock) == 0:  # 자물쇠를 모두 연 경우
                    return True

    return False
