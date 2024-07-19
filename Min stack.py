class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return None

        popped_element = self.stack.pop()

        # If the popped element is equal to the current minimum, update the minimum stack
        if popped_element == self.minstack[-1]:
            self.minstack.pop()

        return popped_element

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.minstack:
            return None
        return self.minstack[-1]

obj = MinStack()
obj.push(3)
obj.push(5)
obj.push(2)
obj.push(1)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()

print("Top element:", param_3)
print("Minimum element:", param_4)
