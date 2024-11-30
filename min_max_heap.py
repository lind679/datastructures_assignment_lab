import heapq

class MinHeap:
    # Class to represent a minimum heap.
    
    def __init__(self):
        self.heap = []  # List to store heap elements

    def push(self, data):
        # Add an element to the heap.
        heapq.heappush(self.heap, data)
        print(f"Added {data} to Min Heap.")

    def pop(self):
        # Remove and return the smallest element from the heap.
        if not self.heap:
            print("Heap is empty. Cannot pop.")
            return None
        popped_data = heapq.heappop(self.heap)
        print(f"Popped {popped_data} from Min Heap.")
        return popped_data

    def peek(self):
        # Get the smallest element without removing it.
        if not self.heap:
            print("Heap is empty.")
            return None
        return self.heap[0]

    def display(self):
        # Display the heap elements.
        if not self.heap:
            print("Heap is empty.")
            return
        print("Min Heap elements:", self.heap)


class MaxHeap:
    # Class to represent a maximum heap.

    def __init__(self):
        self.heap = []  # List to store heap elements

    def push(self, data):
        # Add an element to the heap (inverted for max heap).
        heapq.heappush(self.heap, -data)  # Invert the value to simulate max heap
        print(f"Added {data} to Max Heap.")

    def pop(self):
        # Remove and return the largest element from the heap.
        if not self.heap:
            print("Heap is empty. Cannot pop.")
            return None
        popped_data = -heapq.heappop(self.heap)  # Invert the value to get original
        print(f"Popped {popped_data} from Max Heap.")
        return popped_data

    def peek(self):
        # Get the largest element without removing it.
        if not self.heap:
            print("Heap is empty.")
            return None
        return -self.heap[0]  # Invert the value to get original

    def display(self):
        # Display the heap elements.
        if not self.heap:
            print("Heap is empty.")
            return
        print("Max Heap elements:", [-x for x in self.heap])  # Invert the values for display


# Example usage
if __name__ == "__main__":
    print("Min Heap Operations:")
    min_heap = MinHeap()
    min_heap.push(10)
    min_heap.push(20)
    min_heap.push(5)
    min_heap.push(30)
    min_heap.display()
    print(f"Peek (Min): {min_heap.peek()}")
    min_heap.pop()
    min_heap.display()

    print("\nMax Heap Operations:")
    max_heap = MaxHeap()
    max_heap.push(10)
    max_heap.push(20)
    max_heap.push(5)
    max_heap.push(30)
    max_heap.display()
    print(f"Peek (Max): {max_heap.peek()}")
    max_heap.pop()
    max_heap.display()
