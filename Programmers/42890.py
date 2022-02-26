from itertools import combinations


def solution(relation):
    answer = 0
    degree = len(relation[0])  # 속성의 수

    def check_uniqueness(key):
        """
        후보키가 될 수 있는 속성의 튜플을 받아 유일성을 만족하는지 확인하는 함수
        """

        # 후보키가 될 수 있는 속성에 해당하는 값을 하나의 문자열로 기록하고
        # 이를 세트에 저장하여 그 값이 유일한지 판별
        value_set = set()
        for r in relation:
            value = ""
            for k in key:  # 문자열 생성
                value += r[k]

            if value in value_set:  # 값이 유일하지 않은 경우
                return False

            value_set.add(value)
        return True

    # 후보키가 될 수 있는 속성의 인덱스를 튜플로 묶어 저장하는 세트
    index_set = set()

    def check_minimality(key):
        """
        후보키가 될 수 있는 속성의 인덱스를 받아 최소성을 만족하는지 확인하는 함수
        """
        for existed_key in index_set:
            # 만약 세트에 존재하는 후보키와 현재 키의 합집합이 현재 키와 같다면 최소성 어김
            if set(existed_key) | set(key) == set(key):
                return False

        index_set.add(key)
        return True

    for cnt in range(1, degree + 1):
        # 후보키가 될 수 있는 속성의 모든 조합
        possible_key_list = combinations(range(degree), cnt)

        for possible_key in possible_key_list:
            # 유일성과 최소성을 만족시키는 경우 정답 갱신
            if check_uniqueness(possible_key) and check_minimality(possible_key):
                answer += 1

    return answer
