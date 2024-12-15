class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indices=[]
        for index,word in enumerate(words):
            if x in word:
                indices.append(index)
        return indices
