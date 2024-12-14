class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        n = len(operations)
        X = 0
        for i in range(n):
            if operations[i] == '++X' or operations[i] == 'X++':
                X += 1
            else:
                X -= 1
        return X
