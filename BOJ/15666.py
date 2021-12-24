# 15666. N과 M (12)


def make_sequence(num_cnt, cur_sequence):
    if num_cnt == M:  # 길이가 M인 순열을 생성한 경우
        # 이미 생성된 순열이 아닌 경우 출력
        if tuple(cur_sequence) not in made_sequences:
            print(' '.join(map(str, cur_sequence)))
            made_sequences.add(tuple(cur_sequence))
        return

    for idx in range(0, N):
        # 현재 순열에 숫자가 없거나 마지막 숫자보다 현재 인덱스의 숫자가
        # 크다면 현재 인덱스의 숫자를 포함한다
        if not cur_sequence or cur_sequence[-1] <= num_list[idx]:
            make_sequence(num_cnt + 1, cur_sequence + [num_list[idx]])


N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()  # 오름차순 정렬
made_sequences = set()  # 생성한 순열 저장 세트
make_sequence(0, [])