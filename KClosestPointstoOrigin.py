#Another approach at end

import heapq
import math  

def kClosest(points, k):
    
    min_heap = []
    for i, point in enumerate(points):
        distance = math.sqrt(point[0]**2 + point[1]**2)  
        heapq.heappush(min_heap, (distance, i, point))

    # Step 2: Select top k closest points from min heap
    closest_points = []
    for _ in range(k):
        _, _, point = heapq.heappop(min_heap)  # Extract point using tuple unpacking
        closest_points.append(point)

    return closest_points
'''
The syntax _, _, point = ... is tuple unpacking. 
It allows us to assign the values of the tuple returned by heappop to individual variables.
Here, we use _ for the first two values (distance and index) 
because we don't need them in this context.
 The underscore _ is commonly used as a placeholder for values that we want to ignore.
The point variable receives the third value from the tuple, 
which is the actual point (e.g., [x, y] coordinates).
'''
# Example Usage
points_list = [[1, 3], [-2, 2], [5, 8], [0, 1], [1, -1]]
k = 3
closest_points = kClosest(points_list, k)
print("Top", k, "closest points to origin:", closest_points)















import math

def kClosest(points, k):
    # Step 1: Calculate distances and store points with distances
    points_with_distances = [(point, math.sqrt(point[0]**2 + point[1]**2)) for point in points]

    # Step 2: Sort points based on distances in ascending order
    points_with_distances.sort(key=lambda x: x[1])  # Sort based on distances

    # Step 3: Select top k closest points
    closest_points = [point[0] for point in points_with_distances[:k]]

    return closest_points

# Example Usage
points_list = [[1, 3], [-2, 2], [5, 8], [0, 1], [1, -1]]
k = 3
closest_points = kClosest(points_list, k)
print("Top", k, "closest points to origin:", closest_points)
