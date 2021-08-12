# 1654. 랜선 자르기


# 문제 분류에서 힌트를 얻어 binary search 사용
def cut_lan(n, k, lan_list):
    # 탐색의 우측 값은 랜선 길이 총 합을 원하는 갯수로 나는 것
    total = 0    # 랜선 길이 총 합을 구하기 위한 변수
    for i in range(K):
        total += lan_list[i]
    l = 1    # 탐색의 좌측 값
    r = total // n    # 탐색의 우측 값

    valid_result = []    # 가능한 랜선 길이를 저장할 리스트

    while l <= r:    # binary search 시작
        c = (l + r) // 2    # 자를 랜선 길이 변수
        cnt = 0    # 잘린 랜선 갯수 변수
        for j in range(k):    # 잘린 갯수 총 합
            cnt += lan_list[j] // c
        if n <= cnt:    # 만약 갯수가 같거나 넘치면 valid
            l = c + 1
            valid_result += [c]    # 리스트에 저장해둠
        else:    # 갯수가 부족하면 범위 다시 갱신
            r = c - 1

    # valid 리스트의 맨 마지막 값이 가장 큰 랜선 길이가 됨
    return valid_result[-1]


K, N = map(int, input().split())
my_lan_list = [int(input()) for _ in range(K)]
print(cut_lan(N, K, my_lan_list))