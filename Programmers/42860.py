# 42860. 조이스틱


def solution(name):
    answer = 0

    # 검사된 인덱스를 기록하는 비트 마스킹
    # 0번 인덱스에서 시작되므로 초깃값으로 (1 << 0)을 갖는다
    initial_bit_mask = 1
    for i, v in enumerate(name):
        # 각 인덱스의 알파벳을 만들기 위해 필요한 동작 횟수 추가
        answer += min(ord(v) - ord('A'), abs(ord(v) - ord('Z') - 1))

        # A는 검사할 필요가 없으므로 이미 검사되었다고 표시
        if v == 'A':
            initial_bit_mask |= 1 << i

    # A를 제외한 모든 알파벳을 검사하는데 필요한 최소 동작 횟수
    # 최댓값은 문자열의 길이이므로 이를 초깃값으로 설정
    min_move = len(name) - 1

    # 모든 동작을 (현재 인덱스, 동작 횟수, 비트 마스킹) 양식으로 저장할 리스트
    move_list = [(0, 0, initial_bit_mask)]  # 초깃값 추가

    while move_list:
        # 현재 인덱스, 동작 횟수, 비트 마스킹
        cur_idx, move_cnt, bit_mask = move_list.pop()

        # 만약 현재까지의 동작 횟수가 최솟값보다 크거나 같다면 더이상 탐색할 필요 없음
        if min_move <= move_cnt:
            continue

        # 만약 현재 모든 인덱스가 탐색된 경우 정답에 최솟값 갱신
        if bit_mask == (1 << len(name)) - 1:
            min_move = min(min_move, move_cnt)

        # 현재 인덱스에서 한 칸 전진하는 경우(인덱스 증가)
        move_list.append(((cur_idx + 1) % len(name), move_cnt + 1, bit_mask | (1 << ((cur_idx + 1) % len(name)))))

        # 현재 인덱스에서 한 칸 후진하는 경우(인덱스 감소)
        if cur_idx == 0:
            move_list.append((len(name) - 1, move_cnt + 1, bit_mask | (1 << (len(name) - 1))))
        else:
            move_list.append((cur_idx - 1, move_cnt + 1, bit_mask | (1 << (cur_idx - 1))))

    answer += min_move
    return answer