# 42584. 주식가격


def solution(prices):
    # 1초 뒤에 가격이 떨어진 경우 기간이 1이기에 초기값을 1로 설정
    answer = [1] * len(prices)

    stack = []
    for idx, price in enumerate(prices):
        # 스택에 쌓인 마지막 가격이 현재 가격을 초과하는 경우 즉, 가격이 떨어진 경우
        if stack and price < stack[-1][1]:
            stack.pop()  # 1초 뒤에 가격이 떨어진 경우 기간은 1

            # 스택에 쌓인 마지막 가격이 현재 가격을 초과하는지 다시 탐색
            while stack and price < stack[-1][1]:
                # 1초 이후 가격이 떨어진 경우 기간은 인덱스의 차
                pre_idx = stack.pop()[0]
                answer[pre_idx] = idx - pre_idx

        stack.append((idx, price))  # 스택에 (가격의 인덱스, 가격) 튜플을 추가

    # 스택에 남은 가격은 끝까지 떨어지지 않았으며 그 기간은 마지막 인덱스와 인덱스의 차
    for idx, price in stack:
        answer[idx] = len(prices) - 1 - idx

    return answer