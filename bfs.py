#Implemenation of BFS

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