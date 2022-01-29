# 60057. 문자열 압축


def solution(s):
    answer = len(s) 

    for length in range(1, len(s) // 2 + 1):
        idx = 0  # 검사하는 문자열의 시작 인덱스
        last_word = ''  # 직전에 검사한 문자열 저장
        temp = 0  # 이번 length에서 만들어지는 길이
        same = 0  # 이번 length에서 같은 문자열이 나오는 횟수
        num_length = 10  # same에 따라 자리수를 계산하기 위한 변수
        
        while idx + length <= len(s):
            # 만약 answer를 넘어가면 더 탐색할 필요 없음
            if answer < temp:
                break
            
            # 직전 문자열과 현재 문자열이 같은 경우
            if s[idx: idx + length] == last_word:
                # 연속되어 같은 문자열이 나오고 있는 경우
                if same:
                    same += 1
                    # 만약 같은 문자열이 나온 횟수의 자리수가 1 이상일 경우
                    if num_length <= same:
                        temp += 1
                        num_length *= 10
                
                # 두 문자열이 같은 경우가 처음 등장한 경우
                else:
                    temp += 1 
                    same += 2 
            
            # 직전 문자열과 현재 문자열이 같지 않은 경우 변수를 초기화하고
            # length만큼 답에 추가
            else:
                last_word = s[idx: idx + length]
                same = 0
                num_length = 10
                temp += length

            idx += length
        
        # length만큼 검사할 수 없어 건너 뛴 문자열 부분을 추가
        temp += max(0, len(s) - idx)
        
        # 정답 갱신
        answer = min(temp, answer)
    return answer