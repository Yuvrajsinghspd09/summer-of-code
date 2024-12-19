
# optimal solution
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # it is a simple 2 step problem
        #1. need to swap elements of every row
        #2. performing NOT operation on every element to inverse the image
        
        for row in image:
            n=len(row)
            for i in range((n+1)//2):
                row[i],row[n-i-1]= 1-row[n-i-1], 1- row[i]
        return image


# simpler approach
class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for i in range(len(image)):
            # Reverse the row
            image[i] = image[i][::-1]
            # Invert the row
            image[i] = [1 - x for x in image[i]]
        return image
