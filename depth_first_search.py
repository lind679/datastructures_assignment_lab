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

    def dfs_recursive(self, start, visited=None):
        """Performs DFS recursively starting from the 'start' node."""
        if visited is None:
            visited = set()  # Initialize visited set
        
        # Visit the current node and print it
        visited.add(start)
        print(start, end=" ")

        # Visit all unvisited neighbors
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    def dfs_iterative(self, start):
        """Performs DFS iteratively using a stack starting from the 'start' node."""
        visited = set()  # Set to track visited nodes
        stack = [start]  # Stack to store the nodes to visit

        while stack:
            node = stack.pop()  # Pop the node from the stack
            
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                
                # Add all unvisited neighbors to the stack
                # Reverse the neighbors to visit them in the correct order
                for neighbor in reversed(self.graph[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)

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

    # Perform DFS traversal (Recursive approach)
    print("DFS Recursive Traversal:")
    g.dfs_recursive(1)
    print()

    # Perform DFS traversal (Iterative approach)
    print("DFS Iterative Traversal:")
    g.dfs_iterative(1)
