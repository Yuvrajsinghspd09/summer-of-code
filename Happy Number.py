# optimal approach
class Solution:
    def sum_of_squares(self, n: int) -> int:
      total=0
      while n>0:
        digit=n%10
        total+= digit*digit
        n=n//10
      return total

    def isHappy(self, n: int) -> bool:
        fast = n
        slow = n
        while fast != 1 and self.sum_of_squares(fast) != 1:

            slow = self.sum_of_squares(slow)
            fast = self.sum_of_squares(self.sum_of_squares(fast))
           
            if slow == fast:
                return False
        return True



# better approach
class Solution:
    def sum_of_squares(self, n: int) -> int:
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total

    def isHappy(self, n: int) -> bool:
        seen_numbers = set()
        while n != 1 and n not in seen_numbers:
            seen_numbers.add(n)
            n = self.sum_of_squares(n)
        return n == 1



# brute force
class Solution:
    def sum_of_squares(self, n: int) -> int:
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total

    def isHappy(self, n: int) -> bool:
        seen_numbers = []
        while n != 1 and n not in seen_numbers:
            seen_numbers.append(n)
            n = self.sum_of_squares(n)
        return n == 1
