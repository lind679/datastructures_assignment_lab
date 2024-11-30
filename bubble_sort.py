def bubble_sort(arr):
    n = len(arr)

    for i in range (n):
        for j in range (0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__  == "__main__":
    sample_list = [45, 3, 7, 1, 6]
    print("Sample list is:",sample_list)
    bubble_sort(sample_list)
    print("The Sorted list is:",sample_list)