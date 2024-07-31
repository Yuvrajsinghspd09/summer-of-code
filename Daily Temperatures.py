'''
What the problem asks for:
The "Daily Temperatures" problem asks us to find, for each day, how many days you have to wait until a warmer temperature. It's not asking for the index of the warmer day, but rather the number of days between the current day and the warmer day.
What i and index represent:

i is the current day (or index) we're processing in the main loop.
index is the day (or index) we popped from the stack, which represents a previous day with a cooler temperature.


Why i - index:

The difference i - index gives us the number of days between the current warmer day (i) and the previous cooler day (index).
This difference is exactly what the problem is asking for: how many days you have to wait from the cooler day to reach a warmer day.





'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        return result
