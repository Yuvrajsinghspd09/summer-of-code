from collections import defaultdict

def printGraph(V, edges):
    """
    Function to create an adjacency list for an undirected graph.
    
    Args:
        V (int): The number of vertices in the graph.
        edges (list): A list of lists representing the edges in the graph.
                      Each inner list contains two integers representing
                      the vertices connected by an edge.
    
    Returns:
        dict: The adjacency list representation of the graph.
    """
    # Create an empty dictionary to store the adjacency list
    adj_list = defaultdict(list)
    
    # Iterate over the edges
    for u, v in edges:
        # Add v to the adjacency list of u
        adj_list[u].append(v)
        # Add u to the adjacency list of v (undirected graph)
        adj_list[v].append(u)
    
    # Convert the defaultdict to a regular dictionary
    adj_list = dict(adj_list)
    
    return adj_list



# Example graph with 5 vertices and 5 edges
V = 5
edges = [[0, 1], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]

adj_list = printGraph(V, edges)
print(adj_list)

# The Output
#{0: [1, 4], 1: [0, 2, 3, 4], 2: [1, 3], 3: [1, 2, 4], 4: [0, 1, 3]}