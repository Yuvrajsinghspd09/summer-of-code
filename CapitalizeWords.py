def capitalize_words(s):
    words = s.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

# Test the function
input_str = "hello world"
print(capitalize_words(input_str))  # Output: "Hello World"