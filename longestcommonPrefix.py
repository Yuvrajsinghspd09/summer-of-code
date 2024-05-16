def longest_common_prefix(strings):   #2nd Method below this one
    # Step 1: Check if the array is empty
    if not strings:
        return ""

    # Step 2: Sort the array of strings
    strings.sort()

    # Step 3: Compare the first and last strings
    first_string = strings[0]
    last_string = strings[-1]

    # Step 4: Find the common prefix
    i = 0
    while i < len(first_string) and i < len(last_string) and first_string[i] == last_string[i]:
        i += 1

    return first_string[:i]
'''
def longest_common_prefix(strings):
    if not strings:
        return ""

    for i, column_chars in enumerate(zip(*strings)):
        if len(set(column_chars)) > 1:
            break
    else:
        i += 1

    return strings[0][:i]

'''