def merge_sort(arr):
    # Function to implement the merge sort algorithm.
    if len(arr) <= 1:
        return arr
    
    # Find the middle point and divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Merge the sorted halves and return the result
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """Function to merge two sorted lists into one sorted list."""
    merged = []
    i = j = 0
    
    # Merge the two sorted lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # If there are remaining elements in either left or right list, add them to merged
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged


# Example usage
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Original array:", arr)
    
    sorted_arr = merge_sort(arr)
    
    print("Sorted array:", sorted_arr)

