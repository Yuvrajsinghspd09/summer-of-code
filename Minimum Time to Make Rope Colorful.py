class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0  # Variable to store the total removal time
        current_sum = 0  # Sum of removal times for the current group
        current_max = 0  # Maximum removal time in the current group
        
        # Iterate through colors and neededTime simultaneously
        for i in range(len(colors)):
            # If this is the start of a new group (or the first balloon)
            if i == 0 or colors[i] != colors[i-1]:
                # Add the difference between sum and max of the previous group to total_time
                total_time += current_sum - current_max
                # Reset current_sum and current_max for the new group
                current_sum = neededTime[i]
                current_max = neededTime[i]
            else:
                # If it's the same color as previous, update sum and max
                current_sum += neededTime[i]
                current_max = max(current_max, neededTime[i])
        
        # Add the last group's contribution
        total_time += current_sum - current_max
        
        return total_time