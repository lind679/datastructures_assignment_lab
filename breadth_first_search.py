from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}  # Dictionary to store the graph

    def add_edge(self, u, v):
        """Adds an edge to the graph."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # Since it's an undirected graph

    def bfs(self, start):
        """Breadth-First Search (BFS) starting from the 'start' node."""
        visited = set()  # Set to track visited nodes
        queue = deque([start])  # Queue to store nodes to visit

        visited.add(start)
        print("BFS Traversal:", end=" ")

        while queue:
            node = queue.popleft()  # Dequeue the node
            print(node, end=" ")

            # Enqueue unvisited neighbors
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Example usage
if __name__ == "__main__":
    # Create a graph instance
    g = Graph()

    # Add edges to the graph (undirected graph)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)
    g.add_edge(3, 7)

    # Perform BFS traversal starting from node 1
    g.bfs(1)
