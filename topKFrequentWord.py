'''
Use a hash map to count the frequencies of each word in the list.
Key: Word
Value: Frequency
'''
def topK_frequent(words,k):
    word_freq={}
    for word in words:
        if word in word_freq:
            word_freq[word]+=1
        else:
            word_freq[word]=1

    sorted_words = sorted(word_freq.keys(), key=lambda x: (-word_freq[x], x))
    return sorted_words[:k]
'''
word_freq.keys(): This retrieves all the keys (words) from the word_freq dictionary. It represents the list of unique words in the input list.
lambda x: (-word_freq[x], x): This is a lambda function used as the key function for sorting. 
Let's break it down further:
x: Represents each word from the list of keys (words).
word_freq[x]: Retrieves the frequency of the word x from the word_freq dictionary.
-word_freq[x]: Negates the frequency value. This is done because we want to sort in descending order of frequencies.
(word_freq[x], x): Creates a tuple with the negative frequency and the word itself. This tuple comparison ensures that if two words have the same frequency, they are sorted lexicographically (in ascending order).
'''

words_list = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 3
top_k_frequent = topK_frequent(words_list, k)
print("Top", k, "frequent words:", top_k_frequent)

'''
Time Complexity:
Counting word frequencies using a hash map: O(n), where n is the number of words.
Sorting: O(n log n), where n is the number of words.
Selecting top k words: O(k), as we select the top k words from the sorted list.
Overall, the time complexity is O(n log n) due to sorting, where n is the number of words in the list.

Space Complexity:
Hash map to store word frequencies: O(n), where n is the number of words.
Sorted list: O(n), where n is the number of words.
The space complexity is O(n) due to the hash map and sorted list used in the algorithm.
'''