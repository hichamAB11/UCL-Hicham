
def reachable(adj_list, start_node):
    visited = set()

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in adj_list[node]:
            dfs(neighbor)

    dfs(start_node)
    return visited

adj_list = [[1, 3], [2], [0], [4], [3], []]

print("Reachable from node 0:", reachable(adj_list, 0))
print("Reachable from node 3:", reachable(adj_list, 3))