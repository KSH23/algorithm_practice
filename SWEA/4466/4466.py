"""
4466: 최대 성적표 만들기
"""

import sys
sys.stdin = open('4466_input.txt')


def max_scores(k, scores):
    # 받은 점수 리스트를 내림차순으로 정렬
    sorted_scores = sorted(scores, reverse=True)

    result = 0

    for i in range(k):
        result += sorted_scores[i]

    return result


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    my_scores = list(map(int, input().split()))

    print(f'#{tc} {max_scores(K, my_scores)}')