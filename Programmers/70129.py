# 70129. 이진 변환 반복하기


def solution(s):
    answer = [0, 0]
    
    while s != "1":
        cnt = 0  # 0의 갯수
        for num in s:
            if num == "0":
                cnt += 1
        answer[0] += 1  # 이진 변환 횟수
        answer[1] += cnt  # 제거된 0의 갯수
        s = bin(len(s) - cnt)[2:]  # 이진 변환 결과 갱신
        
    return answer