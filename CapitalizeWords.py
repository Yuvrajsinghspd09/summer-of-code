def capitalize_words(s):
    words = s.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

# Test the function
input_str = "hello world"
print(capitalize_words(input_str))  # Output: "Hello World"

def cap_words(sentence):
    words = sentence.split()
    cap_words= [ words.capitalize() for words in sentence]
    return ''.join(cap_words)
