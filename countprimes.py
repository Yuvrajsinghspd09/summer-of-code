def countPrimes(n):
    if n < 3:
        return 0

    primes = [True] * n
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False

    return sum(primes)

# time complexity :O(N∗Log(Log(N)))
#Space Complexity O(N)

def count_prime(n):
    if n<3:
        return 0
    primes = [True]*n
    primes[0]=primes[1]=False

    for i in range(2,int(n**2)+1):
        if primes[i]:
            for j in range(i*i,n,i):
                primes[j]=False
    return sum(primes)
