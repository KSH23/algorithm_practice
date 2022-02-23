# 42578. 위장


from collections import defaultdict


def solution(clothes):
    answer = 1
    
    # 의상의 종류를 key, 가짓수를 value로 갖는 딕셔너리 생성
    items = defaultdict(int)
    for cloth, category in clothes:
        items[category] += 1
        
    # 의상의 종류는 선택하지 않는 경우와 선택하는 경우가 있으며
    # 선택하는 경우는 옷의 가짓수를 모두 포함하므로
    # 각 의상의 종류에 포함되는 (옷의 가짓수 + 1)을 곱함
    for value in items.values():
        answer *= (value + 1)
    
    # 아무것도 입지 않는 경우 제외
    return answer - 1