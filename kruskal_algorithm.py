class DisjointSet:
    def __init__(self, n):
        """Initialize the disjoint-set (union-find) structure."""
        self.parent = list(range(n))  # Each node is its own parent initially
        self.rank = [0] * n  # Rank to keep the tree flat

    def find(self, u):
        """Find the representative of the set containing 'u'."""
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        """Union the sets containing 'u' and 'v'."""
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank: attach the smaller tree to the root of the larger tree
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

class Kruskal:
    def __init__(self, vertices):
        """Initialize the Kruskal's algorithm with the number of vertices."""
        self.V = vertices  # Number of vertices
        self.edges = []  # List of edges in the graph

    def add_edge(self, u, v, weight):
        """Add an edge to the graph."""
        self.edges.append((weight, u, v))

    def kruskal_mst(self):
        """Perform Kruskal's algorithm to find the MST."""
        # Step 1: Sort edges by weight
        self.edges.sort()

        # Initialize disjoint set
        disjoint_set = DisjointSet(self.V)

        mst = []  # To store the resulting MST
        total_weight = 0  # Total weight of MST

        # Step 2: Process edges one by one
        for weight, u, v in self.edges:
            # Check if including this edge forms a cycle
            if disjoint_set.find(u) != disjoint_set.find(v):
                disjoint_set.union(u, v)  # Include this edge in MST
                mst.append((u, v, weight))  # Add edge to the MST
                total_weight += weight  # Add its weight to the total weight
            # If we have included (V-1) edges, we can stop
            if len(mst) == self.V - 1:
                break

        return mst, total_weight

# Example usage
if __name__ == "__main__":
    # Number of vertices
    num_vertices = 6
    kruskal = Kruskal(num_vertices)

    # Adding edges (u, v, weight)
    kruskal.add_edge(0, 1, 4)
    kruskal.add_edge(0, 2, 3)
    kruskal.add_edge(1, 2, 1)
    kruskal.add_edge(1, 3, 2)
    kruskal.add_edge(2, 3, 4)
    kruskal.add_edge(3, 4, 5)
    kruskal.add_edge(4, 5, 6)
    kruskal.add_edge(2, 5, 7)

    # Find the Minimum Spanning Tree (MST)
    mst, total_weight = kruskal.kruskal_mst()

    print("Edges in MST:")
    for u, v, weight in mst:
        print(f"{u} - {v}: {weight}")

    print(f"Total weight of MST: {total_weight}")
