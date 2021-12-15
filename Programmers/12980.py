# 12980. 점프와 순간 이동


def solution(n):
    ans = 0

    cur_loc = n  # 현재 위치

    while cur_loc:
        if cur_loc % 2:  # 홀수인 경우
            ans += 1  # 한 칸 뒤로 점프하고
            cur_loc = (cur_loc - 1) // 2  # 순간이동
        else:  # 짝수인 경우
            cur_loc //= 2  # 순간이동

    return ans