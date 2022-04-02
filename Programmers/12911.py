# 12911. 다음 큰 숫자


def solution(n):
    # 1. n을 이진수 문자열로 변환
    n = bin(n)[2:]  # 2진수 변환

    zero_exist = False  # 탐색중 0을 발견한 경우 True

    # 2. n을 우측부터 좌측으로 탐색
    for index in range(len(n) - 1, -1, -1):
        # 2-1. 0을 만난 경우 이를 기록하고 넘어감
        if n[index] == "0":
            zero_exist = True
            continue

        # 3. 1을 만난 경우 처음 마주친 1의 인덱스를 기록하고
        if n[index] == "1":
            first_one_index = index

            # 3. 연속된 1이 끝나는 인덱스를 탐색
            while -1 < index and n[index] == "1":
                index -= 1

            # 4. 만약 이진수를 문자열을 모두 탐색했으며 0이 없던 경우 즉, 1만 존재하는 경우
            if index == -1 and not zero_exist:
                # 4-1. 맨 앞의 1을 10으로 바꾼 뒤 십진수로 변환하여 반환
                return int("10" + n[1:], 2)

            # 5. 0이 존재하는 경우 연속된 1 중 가장 좌측에 있는 1을 좌측의 0과 바꾸고
            #    그 우측은 채울 수 있는 0의 개수 + 채울 수 있는 1의 개수를 추가하여 기록
            one_count = first_one_index - index - 1  # 채울 수 있는 1의 개수
            zero_count = len(n) - first_one_index - 1  # 채울 수 있는 0의 개수
            ret = "10" + "0" * zero_count + "1" * one_count

            # 6. 좌측에 문자열이 더 남은 경우 이를 이어 붙임
            if -1 < index:
                ret = n[:index] + ret

            # 7. 십진수로 변환한 뒤 반환
            return int(ret, 2)
