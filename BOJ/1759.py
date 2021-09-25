# 1759. 암호 만들기


def make_password(idx=0, vowel=0, consonant=0):
    if len(password) == L:    # 암호 길이가 L이 되었을 때
        if vowel >= 1 and consonant >= 2:    # 조건을 만족하면
            print(''.join(password))    # 출력
        return

    for i in range(idx, C):
        password.append(sorted_char[i])    # 암호에 알파벳 추가
        if sorted_char[i] in ['a', 'e', 'i', 'o', 'u']:
            # 모음을 추가한 경우
            make_password(i + 1, vowel + 1, consonant)
        else:
            # 자음을 추가한 경우
            make_password(i + 1, vowel, consonant + 1)
        password.pop()    # 이미 추가했던 알파벳은 다시 제거


L, C = map(int, input().split())
char_list = input().split()
sorted_char = sorted(char_list)    # 주어진 알파벳 리스트를 사전순 정렬
password = []    # 구하고자 하는 암호를 담는 리스트
make_password()    # 암호 만들기 함수 실행