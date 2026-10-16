def dfs(adj_matrix, node):
    if node < 0 or node >= len(adj_matrix):
        return
    stack = [node]
    visited = [False] * len(adj_matrix)
    result = []
    while stack:
        check_node = stack.pop()
        if not visited[check_node]:
            visited[check_node] = True
            result.append(check_node)

            for n in range(len(adj_matrix[check_node])):
                if adj_matrix[check_node][n] == 1:
                    stack.append(n)

    return result

print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1))