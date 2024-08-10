
def Count_Vowels(s):
    count = 0
    vowels = 'aeiouAEIOU'
    for char in s:
        if char in vowels:
            count+=1
    return count

input_str = "Hello World"
print(Count_Vowels(input_str))  # Output: 3 (count of 'e', 'o', and 'o')
