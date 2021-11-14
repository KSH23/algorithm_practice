# 1541. 잃어버린 괄호


import sys


# '-' 등장 이후로는 다 뺄 수 있다
# 마지막 숫자도 for loop 안에서 탐색하기 위해 맨 뒤 문자열 추가
command = sys.stdin.readline().rstrip() + '+'

number = ''  # 숫자 기록 변수
flag = True  # '-'가 등장하면 False 전환
ans = 0  # 최종 정답
for char in command:
    if char.isdigit():  # 숫자인 경우
        number += char
    else:
        if flag:  # '-'가 등장한 적 없는 경우
            ans += int(number)
        else:  # '-'가 등장한 적 있는 경우
            ans -= int(number)

        if char == '-':
            flag = False
        number = ''  # 숫자 string 초기화
print(ans)