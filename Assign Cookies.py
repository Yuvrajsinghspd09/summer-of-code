'''
Time Complexity: O(n log n + m log m)
Space Complexity: O(1)

'''
def findContentChildren(g, s):
    g.sort()  # Sort the greed factors
    s.sort()  # Sort the cookie sizes
    
    i = 0  # Pointer for greed factors
    j = 0  # Pointer for cookie sizes
    content_children = 0
    
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:  # If the current cookie can satisfy the current child
            content_children += 1  # One more child is content
            i += 1  # Move to the next child
        j += 1  # Move to the next cookie regardless of whether the current child was content
    
    return content_children
