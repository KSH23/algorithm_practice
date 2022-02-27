# 76502. 괄호 회전하기


def solution(s):
    answer = 0

    def is_correct(string):
        """
        올바른 괄호 문자열이 되는지 여부를 반환하는 함수
        :param string: 문자열
        :return: True or False
        """
        stack = []
        for letter in string:
            # 여는 괄호는 무조건 스택에 추가
            if letter == "(" or letter == "{" or letter == "[":
                stack.append(letter)
                continue

            # 스택이 비었는데 닫히는 괄호가 들어온 경우
            if not stack and (letter == ")" or letter == "}" or letter == "]"):
                return False

            # 일치하는 열리는 괄호가 스택 최상단에 없는 경우
            if ((letter == ")" and stack[-1] != "(")
                    or (letter == "]" and stack[-1] != "[")
                    or (letter == "}" and stack[-1] != "{")):
                return False

            # 일치하는 열리는 괄호가 스택 최상단에 있는 경우 열리는 괄호 제거
            else:
                stack.pop()

        # 스택에 완성되지 못한 괄호가 남은 경우
        if stack:
            return False

        return True

    for rotate in range(len(s)):
        s = s[1:] + s[0: 1]  # 문자열을 왼쪽으로 회전
        if is_correct(s):
            answer += 1

    return answer
