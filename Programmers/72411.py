# 72411. 메뉴 리뉴얼


import itertools
from collections import defaultdict


def solution(orders, course):
    answer = []
    orders = [sorted(order) for order in orders]

    for size in course:
        # 기본값으로 0을 설정한 딕셔너리
        # key는 메뉴, value는 메뉴가 등장한 횟수
        menu_cnt = defaultdict(int)

        for order in orders:
            # 현재 크기로 만들 수 있는 메뉴의 조합
            result_list = list(itertools.combinations(order, size))

            # 각 메뉴를 딕셔너리에 기록
            for result in result_list:
                menu_cnt[result] += 1

        if menu_cnt.values():
            # 메뉴가 등장한 최대 횟수(2 이상)
            max_cnt = max(menu_cnt.values())
            max_cnt = max(2, max_cnt)

            # 최대 횟수만큼 등장한 메뉴를 정답에 기록
            for k, v in menu_cnt.items():
                if v == max_cnt:
                    answer.append("".join(k))

    return sorted(answer)