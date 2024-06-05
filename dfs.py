'''    
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Initialize the set of visited nodes

    visited.add(start)  # Mark the current node as visited
    print(start)  # Process the current node (or perform any operation)

    for neighbor in graph[start]:  # Explore neighbors of the current node
        if neighbor not in visited:
            dfs(graph, neighbor, visited)  # Recursive DFS call for unvisited neighbors

# Example graph represented as an adjacency list
# For each node, the list contains its neighbors
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

# Starting node for DFS traversal
start_node = 'A'

# Perform DFS traversal starting from the 'start_node'
dfs(graph, start_node)



'''
def dfs(graph,start, visited= None):
    if visited is None:
        visited = set()
        
    visited.add(start)      # .add is a method to add elements in set
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph,neighbor,visited)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

start_node = 'B'
dfs(graph,start_node)

        




'''

# recursive method
def dfs_recursive(graph,start,visited=None):
    if visited is None:
        visited=set()

    visited.add(start)
    print(start)


    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph,neighbor,visited)

'''


'''
def rec_dfs(graph,start,visited=None):
    if visited is not None:
        visited=set():
    
    visited.add(start)
    print(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            rec_dfs(graph,neighbor,visited)



'''


# dfs using stack

'''
def stack_dfs(graph,start):
    visited=set()
    stack=start[]


    while stack:
        vertex=stack.pop()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)


            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)

        return visited

'''
''' 





'''