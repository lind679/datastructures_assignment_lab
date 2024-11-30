def heapify(arr, n, i):
    # Helper function to maintain the heap property.
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # If left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child is larger than root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and recursively heapify the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)


def heap_sort(arr):
    """Function to implement the heap sort algorithm."""
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements from the heap
    for i in range(n - 1, 0, -1):
        # Move current root to the end
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)  # Heapify the reduced heap

    return arr


# Example usage
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Original array:", arr)
    
    sorted_arr = heap_sort(arr)
    
    print("Sorted array:", sorted_arr)
