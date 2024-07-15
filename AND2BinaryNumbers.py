##
def logical_AND(num1, num2):
    # Convert binary strings to integers
    int_num1 = int(num1, 2)
    int_num2 = int(num2, 2)
    
    '''
int_num1 = int(num1, 2): Here, we convert the binary string num1
 to an integer using Python's built-in int() function. 
 The second argument 2 specifies that the string should be interpreted as a binary number. 
The result is stored in the variable int_num1.
'''
    # Perform logical AND
    result = int_num1 & int_num2
    
    # Convert result back to binary string
    return bin(result)[2:]
'''
return bin(result)[2:]: Here, we convert the integer result back
 to a binary string using Python's built-in bin() function. The [2:] slice notation
   is used to remove the '0b' prefix that bin() adds to binary strings. 
   Finally, the function returns the binary string
 representing the result of the logical AND operation.
'''
# Test the function
num1 = "101"
num2 = "110"
print(logical_AND(num1, num2))  # Output: "100"
