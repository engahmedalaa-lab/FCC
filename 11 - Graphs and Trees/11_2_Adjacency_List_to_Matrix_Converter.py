adj_list1 = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [2]
}

def adjacency_list_to_matrix(adj_list: dict):
    n = len(adj_list)
    adj_keys = list(adj_list.keys())
    adj_matrix = []
    result = f""

    for key in adj_keys:
        node_list = []
        for i in range(n):
            if adj_keys[i] in adj_list[key]:
                node_list.append(1)
            else:
                node_list.append(0)
        result += f"{node_list}\n"
        adj_matrix.append(node_list)

    print(result)
    return adj_matrix