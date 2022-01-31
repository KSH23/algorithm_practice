# 12951. JadenCase 문자열 만들기


def solution(s):
    answer = ""
    
    first_letter = True  # 대문자를 넣어야하는 경우 True
    for letter in s.lower():
        if letter == " " or letter.isnumeric() or not first_letter:
            answer += letter
            if letter == " ":  # 새로운 단어 시작
                first_letter = True
            elif letter.isnumeric():  # 숫자를 만나면 대문자 없음
                first_letter = False
        elif first_letter:  # 대문자 추가
            answer += letter.capitalize()
            first_letter = False
    
    return answer