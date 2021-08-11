# 1945. 간단한 소인수분해


def simple_factorization(n):
    check_list = [2, 3, 5, 7, 11]
    result_list = [0, 0, 0, 0, 0]    # 횟수를 저장하는 리스트
    for i in range(5):
        while n % check_list[i] == 0:    # 나머지가 있으면 더이상 나눠지지 않음
            result_list[i] += 1
            n //= check_list[i]

    return result_list


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = ' '.join(map(str, simple_factorization(N)))
    print('#{} {}'.format(tc, result))