import heapq
import sys


def greedy_sssp(graph, source):
    distances = {vertex: sys.maxsize for vertex in graph}
    distances[source] = 0

    # Priority queue to store vertices and their tentative distances
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip if the vertex has already been processed with a shorter distance
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Update the distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Example usage:
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 3, 'B': 2, 'D': 4, 'E': 6},
    'D': {'B': 1, 'C': 4, 'E': 8},
    'E': {'C': 6, 'D': 8}
}

source_vertex = 'A'

shortest_distances = greedy_sssp(graph, source_vertex)

print("Shortest distances from the source vertex:")
for vertex, distance in shortest_distances.items():
    print(f"Vertex: {vertex}, Distance: {distance}")
