# 15663. N과 M (9)


def make_sequence(num_cnt, cur_sequence):
    if num_cnt == M:  # 길이가 M인 순열을 생성한 경우
        made_sequences.add(tuple(cur_sequence))
        return

    for idx in range(0, N):
        if num_check[idx]:  # 이미 사용한 숫자는 무시
            continue

        # 현재 인덱스의 숫자를 포함하는 경우
        num_check[idx] = True
        make_sequence(num_cnt + 1, cur_sequence + [num_list[idx]])
        num_check[idx] = False


N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_check = [False] * N  # 숫자 사용 확인 리스트
made_sequences = set()  # 생성한 순열 저장 세트
make_sequence(0, [])
made_sequences = sorted(list(made_sequences))
for sequence in made_sequences:
    print(' '.join(map(str, sequence)))