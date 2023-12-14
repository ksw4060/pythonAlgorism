# https://www.acmicpc.net/problem/27433
# 팩토리얼 2

N = int(input())


def factorial(N):
    if N == 0:
        return 1
    else:
        return N * factorial(N-1)

print(factorial(N))