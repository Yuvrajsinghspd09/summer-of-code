#another approach below this one
def poweroftwo(n):
    return n>0 and n&(n-1)==0
        
n=2
x= poweroftwo(5)
print(x)

'''
time Complexity: 
O(1) - The bitwise operations are performed in constant time.
Space Complexity: 
O(1) - No additional space is used apart from a few variable
'''

'''  
Iterative Division by 2: Continuously divide 
n by 2 as long as it is even.
Check the Result: If the result after division is 1, 
n is a power of two

def isPowerOfTwo(n: int) -> bool:
    if n <= 0:
        return False
    while n % 2 == 0:
        n //= 2
    return n == 1

'''