# 77886. 110 옮기기


def solution(s):
    answer = []

    for x in s:
        count = 0  # 만들 수 있는 110의 개수
        result = []  # 110을 제외한 나머지 숫자들

        # x에서 만들 수 있는 110을 모두 제거
        for number in x:
            result.append(number)
            if 3 <= len(result) and result[-3:] == ["1", "1", "0"]:
                count += 1
                result.pop()
                result.pop()
                result.pop()

        for index in range(len(result) - 1, -1, -1):  # 110을 제거한 결과를 역순으로 탐색
            if result[index] == "0":  # 0을 만나는 순간 0 뒤로 110을 전부 추가
                answer.append("".join(result[0: index + 1])
                              + "110" * count + "".join(result[index + 1:]))
                break
        else:  # 0이 없는 경우 맨 앞에 110을 전부 추가
            answer.append("110" * count + "".join(result))

    return answer
