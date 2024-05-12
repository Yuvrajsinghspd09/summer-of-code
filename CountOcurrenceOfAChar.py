def count_character(s, char):
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count


input_str = "hello world"
character_to_count = 'o'
result = count_character(input_str, character_to_count)
print("Occurrences of character '{}': {}".format(character_to_count, result))