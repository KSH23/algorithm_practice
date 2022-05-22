# 67258. 보석 쇼핑


from collections import defaultdict


def solution(gems):
    gems = [""] + gems  # 계산 편의를 위해 0번 인덱스에 더미 값 추가
    left, right = 1, 0
    total_gems_count = len(set(gems)) - 1
    gems_count = defaultdict(int)  # 보석의 종루에 따른 개수 기록 딕셔너리

    answer = [1, len(gems) - 1]

    while len(gems_count.keys()) <= total_gems_count and right + 1 < len(gems):
        # 우측 인덱스를 우측으로 이동
        right += 1
        gems_count[gems[right]] += 1

        # 우측 보석을 선택한 결과 모든 종류의 보석을 선택한 경우
        while len(gems_count.keys()) == total_gems_count:
            # 1개를 초과하는 보석을 좌측에서부터 제거하여 구간을 짧게 만듦
            if 1 < gems_count[gems[left]]:
                gems_count[gems[left]] -= 1
                left += 1

            # 보석을 제거할 수 업는 경우 즉 답이 될 수 있는 구간인 경우
            # 답을 최소 구간으로 갱신하고 break
            else:
                if right - left < answer[1] - answer[0]:
                    answer = [left, right]
                break

    return answer
