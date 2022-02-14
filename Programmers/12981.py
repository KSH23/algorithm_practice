# 12981. 영어 끝말잇기


def solution(n, words):
    answer = [0, 0]

    end_letter = words[0][0]  # 끝말
    said_words = set()  # 등장한 단어 기록

    for round in range(len(words) // n):  # 차례
        for person in range(n):  # 사람 번호
            cur_word = words[round * n + person]  # 현재 외친 단어
            
            # 만약 현재 위친 단어가 이미 등장했거나, 끝말을 잇지 못한경우
            if cur_word in said_words or cur_word[0] != end_letter:
                return [person + 1, round + 1]

            said_words.add(cur_word)  # 단어 기록
            end_letter = cur_word[-1]  # 끝말 갱신
            
    return answer