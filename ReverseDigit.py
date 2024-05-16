def reverse(x):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    # Convert integer to string, reverse, and convert back to integer
    reversed_x = int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])

    # Check for overflow
    if reversed_x > INT_MAX or reversed_x < INT_MIN:
        return 0
    
    return reversed_x


#2ND METHOD
def reverse(x):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    reversed_x = 0

    while x != 0:
        digit = x % 10
        reversed_x = reversed_x * 10 + digit
        x = x // 10

    return reversed_x if INT_MIN <= reversed_x <= INT_MAX else 0

# Example usage
x = 123
result = reverse(x)
print(result)  # Output: 321

