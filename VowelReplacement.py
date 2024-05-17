def replaceVowels(input_str, replacement_char):
    vowels = 'aeiouAEIOU'
    replaced_str = ""

    # Iterate through the string and replace vowels
    for char in input_str:
        if char in vowels:
            replaced_str += replacement_char
        else:
            replaced_str += char

    return replaced_str

