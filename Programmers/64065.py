# 64065. 튜플


def solution(s):
    answer = []
    
    # 문자열을 각각의 집합으로 나눈뒤 튜플의 길이를 기준으로 오름차순 정렬
    s = sorted(s[2: -2].split('},{'), key=lambda x: len(x))
    
    checked_num = set()  # 정답 튜플에 포함된 숫자 기록 세트
    
    for tuple in s:
        # 집합 문자열을 각각의 숫자로 나눔
        tuple = map(int, tuple.split(','))
        
        # 집합에 들어있는 숫자에 대하여 정답 튜플에 포함되지 않은 숫자는
        # 정답 튜플과 숫자 기록 세트에 추가
        for num in tuple:
            if num not in checked_num:
                checked_num.add(num)
                answer.append(num)
                
    return answer