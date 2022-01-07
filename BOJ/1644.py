# 1644. 소수의 연속합


N = int(input())

# 에라스토테네스의 체를 위한 소수 판별 리스트
prime_numbers_check = [True] * (N + 1)

# 에라스토테네스의 체를 이용한 소수 판별
# N의 제곱근까지만 검사해도 되는 이유는 다음 링크 참고
# http://sprexatura.blogspot.com/2016/05/n-n-square-root-of-n.html
for num in range(2, int(N ** 0.5) + 1):
    if prime_numbers_check[num]:
        for next_num in range(num * 2, N + 1, num):
            prime_numbers_check[next_num] = False

# 소수를 따로 리스트에 저장
prime_numbers = []
for num in range(2, N + 1):
    if prime_numbers_check[num]:
        prime_numbers.append(num)

left = 0  # 좌측 인덱스
right = -1  # 우측 인덱스
prime_numbers_sum = 0  # 소수의 총 합
ans = 0  # 경우의 수

# 투 포인터를 이용하여 연속된 소수의 합이 N이 되는 경우의 수를 확인
while left < len(prime_numbers) and right < len(prime_numbers):
    if prime_numbers_sum < N:
        right += 1
        if right < len(prime_numbers):  # 인덱스 에러 방지
            prime_numbers_sum += prime_numbers[right]
    elif N < prime_numbers_sum:
        prime_numbers_sum -= prime_numbers[left]
        left += 1
    else:  # prime_numbers_sum == N
        ans += 1
        prime_numbers_sum -= prime_numbers[left]
        left += 1
print(ans)