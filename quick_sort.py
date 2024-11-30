def quick_sort(arr):
    # Function to implement the quick sort algorithm.
    if len(arr) <= 1:
        return arr
    
    # Choose the pivot (we can choose different pivot strategies, here we choose the last element)
    pivot = arr[-1]
    
    # Partition the array into two sub-arrays: smaller and larger than the pivot
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    # Recursively sort the left and right sub-arrays, and combine them with the pivot
    return quick_sort(left) + [pivot] + quick_sort(right)


# Example usage
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Original array:", arr)
    
    sorted_arr = quick_sort(arr)
    
    print("Sorted array:", sorted_arr)
