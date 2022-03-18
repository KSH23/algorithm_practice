# 12924. 숫자의 표현


def solution(n):
    answer = 0

    sum_list = [0]  # 0부터 인덱스 숫자까지 더한 값 저장
    for number in range(1, n + 1):
        sum_list += [sum_list[number - 1] + number]

    start, end = 0, 1
    while start <= n and end <= n:
        # start 숫자부터 end 숫자까지의 합
        number_sum = sum_list[end] - sum_list[start]

        if number_sum == n:
            answer += 1
            start += 1
        elif number_sum < n:
            end += 1
        elif n < number_sum:
            start += 1

    return answer
