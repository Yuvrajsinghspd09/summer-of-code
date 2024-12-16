#approach 1
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            total_wealth = sum(customer)
            max_wealth = max(max_wealth, total_wealth)
        return max_wealth
