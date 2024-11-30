def insertion_sort(arr):
    # Function to implement the insertion sort algorithm.
    n = len(arr)
    
    # Traverse through 1 to len(arr)
    for i in range(1, n):
        key = arr[i]  # The current element to be inserted in the sorted portion
        j = i - 1  # The index of the last element of the sorted portion
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key at the correct position
        arr[j + 1] = key
    
    return arr


# Example usage
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Original array:", arr)
    
    sorted_arr = insertion_sort(arr)
    
    print("Sorted array:", sorted_arr)
