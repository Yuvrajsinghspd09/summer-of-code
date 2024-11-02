'''
Steps:

Sort the array of weights in ascending order.
Initialize two pointers: left at the start (lightest person) and right at the end (heaviest person).
While left <= right:
a. If the sum of weights at left and right is <= limit, pair them and move both pointers.
b. Otherwise, put the heavier person (right) in a boat alone and move the right pointer.
Count the number of boats used.

Time Complexity: O(n log n) due to sorting
'''

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats=0
        left=0
        right=len(people)-1
        while left<=right:
            if people[left]+people[right]<=limit:
                left+=1
                right-=1
                boats+=1
            else:
                right-=1
                boats+=1
        return boats


#practice attempt 1
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n=len(people)
        boats=0
        l=0
        r=n-1
        while l<=r:
            if people[l]+people[r]<= limit:
                boats+=1
                l+=1
                r-=1
            else:
                boats+=1
                r-=1
    
        return boats
                
