# 72412. 순위 검색


from collections import defaultdict
from bisect import bisect_left


def solution(info, query):
    answer = []

    # 지원자의 능력을 key로 분류하고 리스트로 초기값이 설정된 value에 점수를 추가
    info_dict = defaultdict(list)
    for applicant in info:
        applicant = applicant.split(' ')

        # 이후 query에서 등장할 "-" 조건을 고려하여 key 설정
        for lang in [applicant[0], "-"]:
            for pos in [applicant[1], "-"]:
                for exp in [applicant[2], "-"]:
                    for food in [applicant[3], "-"]:
                        info_dict[(lang, pos, exp, food)].append(int(applicant[4]))

    # 원하는 점수를 효율적으로 찾을 수 있도록 점수 오름차순 정렬
    for value in info_dict.values():
        value.sort()

    for q in query:
        q = q.replace("and ", "").split()
        key = tuple(q[0: 4])  # 원하는 조건

        cnt = 0
        if info_dict[key]:
            target_list = info_dict[key]  # 조건을 만족하는 점수의 리스트
            value = int(q[-1])  # 원하는 점수

            # bisect_left를 이용해 lower bound를 구한 뒤 개수 계산
            cnt = len(target_list) - bisect_left(target_list, value)

        answer.append(cnt)

    return answer
