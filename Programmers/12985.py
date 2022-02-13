# 12985. 예상 대진표


def solution(n,a,b):
    # 계산의 편의를 위해 a < b로 설정
    a, b = min(a, b), max(a, b)
    
    # 첫 번째 라운드부터 시작
    answer = 1
    while True:
        # a가 홀수이고 b가 a보다 1이 큰 경우가 같은 라운드
        if a % 2 and b - a == 1:
            return answer
        
        # a와 b가 각각 승리
        a, b = (a + 1) // 2, (b + 1) // 2
        
        # 라운드 증가
        answer += 1