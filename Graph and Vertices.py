import math

def count(n):
    """
    Function to count the number of undirected graphs that can be constructed from n vertices.

    Args:
        n (int): The number of vertices in the graph.

    Returns:
        int: The number of undirected graphs that can be constructed from n vertices.
    """
    # Calculate the number of possible edges in the graph
    num_edges = n * (n - 1) // 2

    # The number of graphs is equal to 2^num_edges
    num_graphs = math.pow(2, num_edges)

    # Convert the result to an integer (if necessary) and return it
    return int(num_graphs)


'''
There are n * (n - 1) / 2 possible edges in an undirected graph with n vertices.
 This is because there are n * (n - 1) ways to choose an ordered pair of distinct vertices
   (i.e., a directed edge),
 but each undirected edge corresponds to two directed edges,
   so we need to divide by 2 to avoid double-counting.

For example, when n = 3, there are 3 possible directed edges ((0, 1), (0, 2), and (1, 2))
 and 3 possible undirected edges ({0, 1}, {0, 2}, and {1, 2}).

Once we know the number of possible edges, 
we can use the formula for the number of subsets of a set to count the number of graphs. The number of subsets of a set with k elements is 2^k, because each subset can be represented by a binary string of length k, where the i-th bit is 1 if the i-th element is in the subset and 0 otherwise.

Therefore, the number of undirected graphs that can be constructed from n vertices 
is 2^(n * (n - 1) / 2), because there are n * (n - 1) / 2 possible edges and each graph can be represented by a subset of these edges.



'''