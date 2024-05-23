def check_palindrome(num):
    if num<0:
        return False
    return str(num)[::-1] == str(num)

num = 212
print(check_palindrome(num))