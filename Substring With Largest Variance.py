# brute force approach - 0(n^3)
class Solution:
    def largestVariance(self, s: str) -> int:
        def variance(substring):
            if not substring:
                return 0
            count={}
            for char in substring:
                if char in count:
                    count[char]+=1
                else:
                    count[char]=1
            
            max_count= max(count.values())
            min_count = min(count.values())
            return max_count-min_count

        n = len(s)
        max_var=0
        
        for i in range(n):
            for j in range(i,n):
                substring = s[i:j+1]
                current_var = variance(substring)
                max_var = max(max_var, current_var)
        
        return max_var
        
