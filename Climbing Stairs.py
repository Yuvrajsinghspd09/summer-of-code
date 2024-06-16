def climbStairs(n):
    if n <= 1:
        return 1
    
    # Initialize the base cases
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    
    # Fill the dp array using the recurrence relation
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

# recursive approach
def climbStairs(n):
    memo = [-1] * (n + 1)
    
    def helper(i):
        if i <= 1:
            return 1
        if memo[i] == -1:
            memo[i] = helper(i - 1) + helper(i - 2)
        return memo[i]
    
    return helper(n)


# practice attempt 1
def climbstairs(n):
    memo=-1*(n+1)

    def helper_func(i):
        if i<=1:
            return 1
        elif memo[i]==-1:
            memo[i]=helper_func(i-1)+helper_func(i-2)
        return memo[i]
    return helper_func(n)


#practice attempt 2
def climb_stairs(num):
    if num<=1:
        return 1

    dp = [0]*(num+1)
    dp[0]=1
    dp[1]=1

    for i in range(2,num+1):
        dp[num]=dp[num-1]+dp[num-2]

    return dp[num]


#practice attempt 3
def rec_climb_stairs(n):
    memo= [-1]*[n+1]
        return 1
    def helper_func(i):
        if n<=1:
            return 1
        elif memo[i]==-1:
            memo[i]=memo[i-1]+memo[i-2]

        return memo[i]
    return helper_func(n)
