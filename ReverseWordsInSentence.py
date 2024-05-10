def rev_sentence(sentence):
    words = sentence.split()
    reversed_sentence = words.reverse()
    #Join the reversed words
    return ' '.join(words)

input_str = "the sky is blue"
output_str =  rev_sentence(input_str)
print(output_str)


'''
Splitting the string into words takes O(n) time and space.
Reversing the list of words takes O(n) time.
Joining the reversed words takes O(n) time.
Overall, the time complexity of the solution is 

and the Space Complexity is O(n) due to the list of words.
'''