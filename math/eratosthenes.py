import math
n = int(input())
primes = [True] * (n + 1)
for i in range(2, int(math.sqrt(n)) + 1):
    j = 2
    while i * j <= n:
        primes[i * j] = False
        j += 1

result = []
for i in range(1, n + 1):
    if primes[i]:
        result.append(i)

print(result)
