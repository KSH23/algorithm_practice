# 42883. 큰 수 만들기


def solution(number, k):
    answer = number
    idx = 0  # 검사를 진행할 인덱스
    for cnt in range(k):
        # 만약 인덱스가 리스트 길이에 도달한다면 가장 뒤의 숫자가 최소 숫자이므로 가장 마지막 숫자를 제거
        if len(answer) <= idx:
            answer = answer[0: len(answer) - 1]

        # 현재 원소보다 다음 원소가 더 크게 되는 인덱스를 찾음
        while idx < len(answer) - 1 and answer[idx] >= answer[idx + 1]:
            idx += 1

        # 현재 원소보다 다음 원소가 더 크다면 해당 원소를 제거
        answer = answer[0: idx] + answer[idx + 1: len(answer) + 1]

        # 제거된 위치의 이전 원소부터 탐색을 반복
        # -1 인덱스가 나오지 않도록 방지
        idx = max(0, idx - 1)

    return answer