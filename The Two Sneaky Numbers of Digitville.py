#first approach
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        return [num for num,count in freq.items() if count>1]


#2nd approach
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen= set()
        dups=set()
        for num in nums:
            if num in seen:
                dups.add(num)
            seen.add(num)
        return list(dups)
