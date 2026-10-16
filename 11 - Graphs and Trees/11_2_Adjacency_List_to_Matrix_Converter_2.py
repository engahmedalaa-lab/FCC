def adjacency_list_to_matrix(adj_list):
    """
    Convert an adjacency list to an adjacency matrix.

    Parameters:
    adj_list (dict): A dictionary where keys are node labels and values are lists of adjacent nodes.

    Returns:
    list: A 2D list representing the adjacency matrix.
    """
    # Get the number of nodes
    nodes = list(adj_list.keys())
    n = len(nodes)

    # Create a mapping from node labels to indices
    node_index = {node: i for i, node in enumerate(nodes)}

    # Initialize the adjacency matrix with zeros
    adj_matrix = [[0] * n for _ in range(n)]

    # Fill the adjacency matrix
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            if neighbor in node_index:  # Ensure the neighbor is a valid node
                i = node_index[node]
                j = node_index[neighbor]
                adj_matrix[i][j] = 1  # Set the edge in the matrix

    return adj_matrix