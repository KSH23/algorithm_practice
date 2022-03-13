# 17684. [3차] 압축


def solution(msg):
    answer = []

    # 1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
    dictionary = dict()
    for i in range(65, 91):
        dictionary[chr(i)] = i - 64
    last_key_num = 27  # 다음에 추가될 단어의 키

    index = 0
    while index < len(msg):
        # 2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
        w = msg[index]
        while index < len(msg) - 1 and w + msg[index + 1] in dictionary:
            index += 1
            w += msg[index]

        # 3. w에 해당하는 사전의 색인 번호를 출력한다.
        answer.append(dictionary[w])

        # 4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
        if index < len(msg) - 1:
            dictionary[w + msg[index + 1]] = last_key_num
            last_key_num += 1

        index += 1

    return answer
