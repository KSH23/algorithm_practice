# 64064. 불량 사용자

import re


def solution(user_id, banned_id):
    # 제재 아이디 패턴과 일치하는 아이디의 인덱스를 기록
    results = [[] for _ in range(len(banned_id))]
    for pattern_index, pattern in enumerate(banned_id):
        for user_index, user in enumerate(user_id):
            p = re.compile("^" + pattern.replace("*", ".") + "$")
            if p.findall(user):
                results[pattern_index].append(user_index)

    selected_id_group = set()  # 제재된 아이디의 인덱스 그룹의 비트마스킹 기록

    # 중복 없이 results에서 만들 수 있는 조합을 탐색
    def find_combination(idx, bit_masking):
        if idx == len(results):
            return selected_id_group.add(bit_masking)

        for banned_user in results[idx]:
            # banned_user가 선택되지 않은 경우 비스마스킹을 갱신
            if not((1 << banned_user) & bit_masking):
                find_combination(idx + 1, (1 << banned_user) | bit_masking)

        return len(selected_id_group)

    return find_combination(0, 0)
