# 12904. 가장 긴 팰린드롬


def is_palindrome(string):
    # 팰린드롬인지 여부를 반환
    for index in range(len(string) // 2 + 1):
        if string[index] != string[len(string) - index - 1]:
            return False
    return True


def solution(s):
    answer = 1
    length = len(s)

    # 문자열을 탐색하며 최장 길이를 구함
    for left in range(length):
        for right in range(length - 1, left, -1):
            if right - left + 1 <= answer:  # 가지치기
                continue
            if is_palindrome(s[left: right + 1]):
                answer = max(answer, right - left + 1)

    return answer
