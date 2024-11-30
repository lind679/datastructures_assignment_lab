def sum_2d_array(array):
    total_sum = 0
    for row in array:
        total_sum += sum(row)
    return total_sum

# Example usage
if __name__ == "__main__":
    array = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("2D Array:")
    for row in array:
        print(row)
    
    result = sum_2d_array(array)
    print(f"The sum of all numbers in the 2D array is: {result}")
