# 86053. 금과 은 운반하기


def solution(a, b, g, s, w, t):
    # 최대 왕복 횟수는 금과 은의 최대치를 각각 1 씩 운반할 때
    answer = 10 ** (9 + 5) * 4
    left, right = 0, 10 ** (9 + 5) * 4

    while left <= right:
        mid = (left + right) // 2

        # mid 시간 안에 도시에 가져갈 수 있는 최대 무게, 최대 금 무게, 최대 은 무게
        w_max, g_max, s_max = 0, 0, 0
        # g_max + s_min = g_min + s_max이므로 따라서
        # a <= g_max & b <= s_max & a + b <= g_max + s_min = g_min + s_max
        # 이와 같은 경우 도시를 건설할 수 있다(참고 https://prgms.tistory.com/101)
        for city in range(len(t)):
            # mid 시간 안에 도시에 도달할 수 있는 횟수
            move = mid // (t[city] * 2)
            if t[city] <= mid % (t[city] * 2):  # 편도 이동이 가능한 경우
                move += 1

            # 매장량을 초과하여 가져가지 않도록 min 함수로 경계 설정
            g_max += min(w[city] * move, g[city])
            s_max += min(w[city] * move, s[city])
            w_max += min(w[city] * move, g[city] + s[city])

        # 도시를 건설할 수 있는 경우
        if a <= g_max and b <= s_max and a + b <= w_max:
            answer = min(answer, mid)
            right = mid - 1
        else:
            left = mid + 1

    return answer
