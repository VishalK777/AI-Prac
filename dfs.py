class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def dfs(self, start):
        visited = set()
        self._dfs_recursive(start, visited)

    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')

        if vertex in self.graph:
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    self._dfs_recursive(neighbor, visited)


g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('E', 'G')

print("DFS:")
g.dfs('A')
print()
