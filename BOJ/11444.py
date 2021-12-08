# 11444. 피보나치 수 6


import sys

sys.setrecursionlimit(100000)


def fibonacci(num):
    if fibonacci_memo.get(num):
        return fibonacci_memo[num]

    if num % 2:  # num이 홀수인 경우
        # F(2n-1) = (F(n))^2 + (F(n-1))^2
        result = fibonacci((num + 1) // 2) ** 2 + fibonacci(num // 2) ** 2
    else:  # num이 짝수인 경우
        # F(2n) = (2(F(n - 1)) + F(n)) * F(n)
        result = (2 * fibonacci((num - 1) // 2) + fibonacci(num // 2)) * fibonacci(num // 2)

    fibonacci_memo[num] = result % 1000000007
    return fibonacci_memo[num]


N = int(input())
fibonacci_memo = dict()
fibonacci_memo[0] = 0
fibonacci_memo[1] = 1
fibonacci_memo[2] = 1
print(fibonacci(N))