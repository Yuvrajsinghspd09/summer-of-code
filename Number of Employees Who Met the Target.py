class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count=0
        for emp_num in hours:
            if emp_num>=target:
                count+=1
        return count
        
