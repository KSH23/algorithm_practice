# 12586. 회문


def palindrome(words, n, m):
    switch = 1
    result = ''

    for k in range(n):
        # 가로줄 확인
        for i in range(n - m + 1):
            for j in range(m // 2):
                if words[k][i + j] != words[k][i + m - 1 - j]:
                    switch = 0
                    break
                else:
                    switch += 1
            if switch == m // 2:
                result = words[k][i:i+m]
                return result

        # 세로줄 확인
        for i in range(n - m + 1):
            for j in range(m // 2):
                if words[i + j][k] != words[i + m - 1 - j][k]:
                    switch = 0
                    break
                else:
                    switch += 1
            if switch == m // 2:
                for idx in range(m):
                    result += words[i + idx][k]
                return result


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    WORDS = [input() for _ in range(N)]
    print('#{} {}'.format(tc, palindrome(WORDS, N, M)))