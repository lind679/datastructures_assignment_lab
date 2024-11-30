import heapq  # For priority queue (min-heap)

class Graph:
    def __init__(self, vertices):
        """Initialize the graph with a number of vertices."""
        self.V = vertices  # Number of vertices
        self.graph = {i: [] for i in range(vertices)}  # Adjacency list to store graph

    def add_edge(self, u, v, weight):
        """Add an edge to the graph (directed, with weight)."""
        self.graph[u].append((v, weight))  # (neighbor, weight)

    def dijkstra(self, start):
        """Run Dijkstra's algorithm from the 'start' node."""
        # Distance from start to each vertex, initialize with infinity
        distances = [float('inf')] * self.V
        distances[start] = 0  # Distance to the start node is 0

        # Priority queue to pick the node with the smallest tentative distance
        pq = [(0, start)]  # (distance, node)
        
        while pq:
            # Get the node with the smallest distance from the priority queue
            current_dist, u = heapq.heappop(pq)

            # If the current distance is already greater than the recorded distance, skip
            if current_dist > distances[u]:
                continue

            # Relax the edges of the current node
            for v, weight in self.graph[u]:
                distance = current_dist + weight
                if distance < distances[v]:  # If a shorter path is found
                    distances[v] = distance
                    heapq.heappush(pq, (distance, v))  # Push the neighbor into the priority queue
        
        return distances

# Example usage
if __name__ == "__main__":
    # Create a graph with 6 vertices
    g = Graph(6)

    # Add edges (u, v, weight)
    g.add_edge(0, 1, 7)
    g.add_edge(0, 2, 9)
    g.add_edge(0, 5, 14)
    g.add_edge(1, 2, 10)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 11)
    g.add_edge(2, 5, 2)
    g.add_edge(3, 4, 6)
    g.add_edge(4, 5, 9)

    # Run Dijkstra's algorithm starting from node 0
    start_node = 0
    distances = g.dijkstra(start_node)

    # Print the shortest distances from the start node to each vertex
    print(f"Shortest distances from node {start_node}:")
    for node, dist in enumerate(distances):
        print(f"Node {node}: {dist}")
