# 3663. 고득점


def solution(name):
    answer = 0
    length = len(name)  # name의 길이

    for letter in name:
        # 각 인덱스의 알파벳을 만들기 위해 필요한 동작 횟수 추가
        answer += min(ord(letter) - ord('A'), abs(ord(letter) - ord('Z') - 1))

    # A를 제외한 모든 알파벳을 검사하는데 필요한 최소 동작 횟수
    # 최댓값은 문자열의 길이이므로 이를 초깃값으로 설정
    min_move = length - 1
    for i in range(length):
        next_i = i + 1  # 현재 알파벳 이후로 처음 만나는 A가 아닌 알파벳의 인덱스
        while next_i < length and name[next_i] == 'A':
            next_i += 1

        # 이동할 수 있는 경우의 수 1. 우측 -> 좌측
        # 이동할 수 있는 경우의 수 2. 좌측 -> 우측
        min_move = min(min_move, i + (i + length - next_i), 2 * (length - next_i) + i)

    answer += min_move
    return answer


T = int(input())
for _ in range(T):
    print(solution(input()))