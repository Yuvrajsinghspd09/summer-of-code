from collections import defaultdict

def countComponents(n, edges):
    """
    Function to count the number of connected components in an undirected graph.
    
    Args:
        n (int): The number of nodes in the graph.
        edges (List[List[int]]): A list of edges in the graph.
    
    Returns:
        int: The number of connected components.
    """
    # Create an adjacency list to represent the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Set to track visited nodes
    visited = set()
    
    # Counter for connected components
    components = 0
    
    # DFS helper function
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    
    # Iterate over all nodes
    for node in range(n):
        if node not in visited:
            dfs(node)
            components += 1
    
    return components