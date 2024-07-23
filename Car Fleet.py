class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Combine position and speed into tuples and sort by position (descending)
        cars = sorted(zip(position, speed), reverse=True)
        
        # Stack to keep track of arrival times of fleet leaders
        stack = []
        
        for pos, spd in cars:
            # Calculate arrival time for current car
            arrival_time = (target - pos) / spd
            
            # If stack is empty or current car arrives later than the car in front
            if not stack or arrival_time > stack[-1]:
                stack.append(arrival_time)
        
        # The number of elements in the stack is the number of fleets
        return len(stack)
