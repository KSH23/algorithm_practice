# 49993. 스킬트리


def solution(pre_skill_tree, skill_trees):
    answer = 0

    # 각 스킬의 아스키 코드를 인덱스로 갖는 리스트에 스킬의 선행스킬을 아스키 코드로 기록
    pre_skills = list(range(91))
    for index, s in enumerate(pre_skill_tree[1:]):
        pre_skills[ord(s)] = ord(pre_skill_tree[index])

    def is_skill_tree_possible(skills):
        """
        스킬 트리의 가능 여부를 반환하는 함수
        """
        used_skill = set()  # 이미 배운 스킬
        for skill in skills:
            current_skill = ord(skill)  # 현재 스킬을 아스키 코드로 변환
            pre_skill = pre_skills[current_skill]  # 선행 스킬

            if pre_skill == current_skill:  # 선행 스킬이 필요 없는 경우
                used_skill.add(current_skill)  # 스킬 학습
                continue

            while True:
                if pre_skill not in used_skill:  # 선행 스킬을 배우지 않은 경우
                    return False

                if pre_skill == pre_skills[pre_skill]:  # 선행 스킬을 이미 배운 경우
                    used_skill.add(current_skill)
                    break

                pre_skill = pre_skills[pre_skill]  # 선행 스킬의 선행 스킬 탐색

        return True

    for skill_tree in skill_trees:
        if is_skill_tree_possible(skill_tree):
            answer += 1

    return answer
