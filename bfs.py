#Implemenation of BFS

'''

When to use DFS and BFS:

DFS:

When you want to explore all possible paths in a graph or tree.
When you want to traverse a graph or tree in a systematic way.
When the graph or tree is relatively deep and you want to explore deep paths first.
When you need to find connected components or cycles in an undirected graph.


BFS:

When you want to find the shortest path between two nodes in an unweighted graph.
When you want to explore the neighbors of a node before moving to the next level.
When the graph is relatively wide and you want to explore all neighbors first.
When you need to find the minimum number of steps or distance between two nodes.



Both DFS and BFS have a time complexity of O(V + E), where V is the number of vertices and E is the number of edges in the graph

'''


'''

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


'''
'''
from collections import deque

def dfs(graph,start):
    visited=set()
    queue= deque([start])
    visited.add(start)

    node= queue.popleft()
    print(node, end=' ')
    
    for neighbor in graph[node]:  # Correct iteration over neighbors
        if neighbor not in visited:
            queue.append(neighbor)
            visited.add(neighbor)

'''
'''
from collections import deque


def bfs1(graph,start):
    visited=set()
    queue= deque[start]
    visited.add(start)

    node = queue.popleft()
    print(node,end='')

    for neighbor in graph[node]:
        if neighbor not in visited:
            queue.append(neighbor)
            visited.add(neighbor)

'''

from collections import deque

def bfs(graph,start):
    visited = set()
    queue = deque[start]

    node = queue.popleft()
    print(node,end='')

    for neighbor in graph[node]:
        if neighbor not in visited:
            queue.append(neighbor)
            visited.add(neighbor)
