#fct
def mat_to_list(adj_mat):
    adj_list = []
    for i in range(len(adj_mat)):
        ngb = []
        for j in range(len(adj_mat[i])):
            if adj_mat[i][j] == 1:
                ngb.append(j)
        adj_list.append(ngb)
    return [adj_list]

# adjacency matrix
adj_mat = [
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

# function Run
adj_list = mat_to_list(adj_mat)

# result
print("Final adjacency list:")
print(adj_list)
