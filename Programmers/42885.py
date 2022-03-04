# 42885. 구명보트


def solution(people, limit):
    answer = 0

    people.sort(reverse=True)  # 계산의 편의를 위해 내림차순 정렬
    left, right = 0, len(people) - 1  # 좌측, 우측 사람의 인덱스

    while left <= right:
        # 좌측과 우측 사람이 모두 보트에 들어갈 수 있는 경우
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1

        else:  # 좌측 사람만 보트에 들어갈 수 있는 경우
            left += 1
        answer += 1  # 보트 수 추가

    return answer
