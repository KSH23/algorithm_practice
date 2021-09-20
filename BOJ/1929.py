# 1929. 소수 구하기


M, N = map(int, input().split())

# 에라토스테네스의 체에 따라 배수를 갖지 않는 최대 소수를 구함
limit = int(N ** (1/2)) + 1

# 인덱스가 자연수를 의미하고 원소가 1이면 소수, 아니면 0이다
prime_list = [1] * (N+1)  

for i in range(2, limit + 1):    # 2부터 limit까지만 진행
    if prime_list[i]:    # 만약 소수라면
        j = 2
        while i * j < N + 1:    # 소수의 배수 인덱스를 모두 0으로 바꿈
            prime_list[i * j] = 0
            j += 1

for i in range(M, len(prime_list)):
    if i == 1:    # 만약 M == 1인 경우 무시
        continue
    if prime_list[i]:    
        print(i)    # 인덱스 즉, 자연수 출력
