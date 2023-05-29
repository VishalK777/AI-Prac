import sys

def min_spanning_tree(graph):
    num_vertices = len(graph)

    # Initialize lists to track the MST and the corresponding weights
    mst = [None] * num_vertices
    key = [sys.maxsize] * num_vertices
    visited = [False] * num_vertices

    # Start from the first vertex
    key[0] = 0
    mst[0] = -1  # Parent of the first vertex is set to -1

    for _ in range(num_vertices - 1):
        # Find the vertex with the minimum key value from the set of unvisited vertices
        min_key = sys.maxsize
        min_index = -1
        for v in range(num_vertices):
            if not visited[v] and key[v] < min_key:
                min_key = key[v]
                min_index = v

        # Add the selected vertex to the MST
        visited[min_index] = True

        # Update the key and parent values of the adjacent vertices
        for v in range(num_vertices):
            if (
                graph[min_index][v] != 0
                and not visited[v]
                and graph[min_index][v] < key[v]
            ):
                key[v] = graph[min_index][v]
                mst[v] = min_index

    return mst


# Example usage
# Adjacency matrix representation of the graph
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0],
]

mst = min_spanning_tree(graph)
print("Minimum Spanning Tree:")
for i in range(1, len(mst)):
    print(f"{i} - {mst[i]}")