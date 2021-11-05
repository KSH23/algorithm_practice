# 15654. N과 M (5)


def sequence(numbers):
    if len(numbers) == M:  # 길이를 충족시킨 경우
        print(' '.join(map(str, numbers)))

    for i in range(0, N):
        if checked[i]:  # 이미 사용한 숫자는 무시
            continue
        checked[i] = True
        sequence(numbers + [num_list[i]])
        checked[i] = False


N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()  # 사전순 출력을 위한 정렬
checked = [False] * N  # 사용한 숫자 표시
sequence([])