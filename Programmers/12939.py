# 12939. 최댓값과 최솟값


def solution(s):
    # 공백을 기준으로 나눈 뒤 정수 변환 후 오름차순 정렬
    s = sorted(list(map(int, s.split(' '))))
    
    # 최소값과 최대값을 문자열로 저장
    answer = f'{s[0]} {s[-1]}'
    return answer