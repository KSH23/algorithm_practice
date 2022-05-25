# 43163. 단어 변환


from collections import deque


def can_change(word_1, word_2):
    # 두 단어를 받아 한 개의 알파벳만 다른 경우 True 반환
    ret = False

    for letter_1, letter_2 in zip(word_1, word_2):
        # 두 단어에서 알파벳이 두 개 이상 다른 경우
        if ret and letter_1 != letter_2:
            return False

        if letter_1 != letter_2:
            ret = True

    return ret


def solution(begin, target, words):
    words = [begin] + words  # 계산 편의를 위해 begin을 좌측에 삽입
    length = len(words)
    begin_index, target_index = 0, 0

    # 각 단어 인덱스에서 변환할 수 있는 인덱스를 리스트에 기록
    edges = [[] for _ in range(length)]
    for index_1 in range(length):
        if words[index_1] == target:
            target_index = index_1

        for index_2 in range(index_1 + 1, length):
            if can_change(words[index_1], words[index_2]):
                edges[index_1].append(index_2)
                edges[index_2].append(index_1)

    if target_index == 0:  # target이 words 안에 없어 변환 불가
        return 0

    answer = 0

    # BFS 시작
    dq = deque([begin_index])
    visited = [False] * length
    visited[begin_index] = True
    while dq:
        answer += 1
        for _ in range(len(dq)):
            current_index = dq.popleft()

            for index in edges[current_index]:
                if index == target_index:
                    return answer
                if not visited[index]:
                    visited[index] = True
                    dq.append(index)
    return 0
