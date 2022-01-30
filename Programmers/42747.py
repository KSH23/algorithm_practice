# 42747. H-Index


def solution(citations):
    # 숫자를 내림차순 정렬
    citations.sort(reverse=True)

    idx = 1  # 현재 논문의 인덱스
    num = citations[0]  # 현재 탐색중인 숫자로 초기값은 최대 논문 인용 횟수
    cnt = 1  # 현재까지의 논문의 개수
    while True:
        # 주어진 조건을 만족하는 경우 현재 탐생중인 수 반환
        if num <= cnt:
            return num

        num -= 1  # 논문 인용 횟수 감소

        # 현재 탐색중인 숫자와 현재 논문의 인덱스가 같은 경우
        while num == citations[idx]:
            cnt += 1  # 현재까지의 논문 개수 증가

            if idx < len(citations) - 1:
                idx += 1  # 우측으로 인덱스 이동
            else:
                break