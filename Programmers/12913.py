# 12913. 땅따먹기


def solution(land):
    current_row = land[0]  # 현재 밟고 있는 행
    for row in land[1: ]:
        next_row = [0, 0, 0, 0]  # 다음 밟을 행
        
        for col in range(4):  # 다음 밟을 열
            for pre_col in range(4):  # 이미 밟은 열
                if col == pre_col:  # 같은 열을 연속해서 밟은 경우
                    continue
                next_row[col] = max(next_row[col], current_row[pre_col] + row[col])

        current_row = next_row[:]  # 현재 밟고 있는 행 갱신

    return max(next_row)