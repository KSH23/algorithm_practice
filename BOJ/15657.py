# 15657. N과 M (8)


def make_sequence(cur_idx, num_cnt, cur_sequence):
    if num_cnt == M:  # 길이가 M인 순열을 생성한 경우
        print(' '.join(map(str, cur_sequence)))
        return

    for idx in range(cur_idx, N):
        # 현재 인덱스의 숫자를 포함하는 경우
        make_sequence(idx, num_cnt + 1, cur_sequence + [num_list[idx]])


N, M = map(int, input().split())
num_list = list(map(int, input().split()))

# 숫자 리스트에서 중복된 값을 없애고 오름차순으로 정렬
num_list = sorted(list(set(num_list)))
make_sequence(0, 0, [])
