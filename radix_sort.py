def counting_sort(arr, exp):
    """Helper function to perform counting sort based on the digit represented by exp."""
    n = len(arr)
    output = [0] * n  # Output array to store sorted values
    count = [0] * 10  # Count array to store the frequency of digits (0-9)

    # Store the count of occurrences in count[]
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Change count[i] so that it now contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array by placing elements in the correct position based on current digit
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output array to arr[], so that arr[] now contains sorted numbers
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    """Function to implement the radix sort algorithm."""
    # Find the maximum number to determine the number of digits
    max_num = max(arr)

    # Perform counting sort for every digit (exp is 10^i for the current digit)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


# Example usage
if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Original array:", arr)
    
    radix_sort(arr)
    
    print("Sorted array:", arr)
