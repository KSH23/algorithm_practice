# 17677. [1차] 뉴스 클러스터링


from collections import defaultdict


def solution(str1, str2):
    # 편의를 위해 두 문자열을 소문자로 변환
    str1, str2 = str1.lower(), str2.lower()

    # 각 문자열의 단어 집합 저장 딕셔너리
    str_dict1, str_dict2 = defaultdict(int), defaultdict(int)
    
    # 각 문자열에서 알파벳으로만 이루어딘 단어를 딕셔너리에 추가하는 함수
    def make_string_dict(string, str_dict):
        for idx in range(len(string) - 1):
            if string[idx].isalpha() and string[idx + 1].isalpha():
                str_dict[string[idx: idx + 2]] += 1

    make_string_dict(str1, str_dict1)
    make_string_dict(str2, str_dict2)
    
    # 교집합의 길이와 합집합의 길이 초기값 설정
    intersect = 0
    union = sum(str_dict1.values()) + sum(str_dict2.values())

    for key, value in str_dict1.items():
        # 만약 공통된 단어를 만나면 교집합의 길이는 추가되고 합집합의 길이는 감소
        if key in str_dict2:
            intersect += min(value, str_dict2[key])
            union -= min(value, str_dict2[key])

    if union:
        return int(65536 * intersect / union)
    else:
        return 65536


