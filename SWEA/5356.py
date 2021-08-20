# 5356. 의석이의 세로로 말해요


def v_str(str_li):
    limit = 0    # 최종 결과와 비교하기 위한 총 글자 수
    for i in range(5):
        limit += len(str_li[i])

    result = ''    # 최종 결과를 저장하는 변수

    i = 0    # 현재 세로열의 인덱스
    while len(result) < limit:    # 총 글자 수를 채울 때 까지 반복
        for j in range(5):
            # 만약 문자열의 길이가 현재 세로열의 인덱스보다 작으면 넘어감
            if len(str_li[j]) < i + 1:
                continue
            else:    # 그렇지 않다면 최종 결과에 추가
                result += str_li[j][i]
        i += 1    # 세로열의 인덱스를 한 칸 우측으로 밀어줌

    return result


T = int(input())
for tc in range(1, T+1):
    str_list = [input() for _ in range(5)]
    print('#{} {}'.format(tc, v_str(str_list)))
