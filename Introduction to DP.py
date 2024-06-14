#Top-Down Approach (Memoization):

def topDown(n, dp={0: 0, 1: 1}):
    MOD = 10**9 + 7
    if n in dp:
        return dp[n]
    
    dp[n] = (topDown(n-1, dp) + topDown(n-2, dp)) % MOD
    #We use the modulo operator % to ensure the result doesn't exceed the given constraint.
    return dp[n]





def bottomUp(n):
    MOD = 10**9 + 7
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
    
    return dp[n]




#practice attempt 1
def top_down(n,dp={0:0,1:1}):
    MOD = 10**9+7
    if n in dp:
        return dp[n]
    
    dp[n]= (top_down(n-1,dp)+top_down(n-2,dp))%MOD
    return dp[n]

