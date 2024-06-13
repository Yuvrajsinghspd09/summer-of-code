def AllPrimeFactors(N):
    prime_factors = []
    
    # Check for smallest prime factors from 2 to sqrt(N)
    i = 2
    while i < int(N**0.5) + 1:
        if N % i == 0:
            # If i is a prime factor, add it to the list
            prime_factors.append(i)
            
            while N % i == 0:
                N //= i
        i += 1
    
    # If there's any prime factor greater than sqrt(N), it will be left in N
    if N > 1:
        prime_factors.append(N)
    
    return prime_factors
