def max_subarray_sum(numbers):
    """
    Find the maximum sum of a contiguous subarray using Kadane's Algorithm.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        numbers: List of integers
        
    Returns:
        int: Maximum sum of contiguous subarray
        
    Examples:
        >>> max_subarray_sum([-1, 5, -3, 9, -11])
        11
        >>> max_subarray_sum([9])
        9
        >>> max_subarray_sum([1, 2, 3, 4])
        10
    """
    if not numbers:
        return 0
    
    # Initialize with the first element
    max_sum = numbers[0]
    current_sum = numbers[0]
    
    # Iterate through the rest of the array
    for i in range(1, len(numbers)):
        # Either extend the existing subarray or start a new one
        current_sum = max(numbers[i], current_sum + numbers[i])
        # Update the maximum sum found so far
        max_sum = max(max_sum, current_sum)
    
    return max_sum


def max_subarray_sum_with_indices(numbers):
    """
    Find the maximum sum of a contiguous subarray and return the indices.
    
    Args:
        numbers: List of integers
        
    Returns:
        tuple: (max_sum, start_index, end_index)
    """
    if not numbers:
        return 0, -1, -1
    
    max_sum = numbers[0]
    current_sum = numbers[0]
    start = 0
    end = 0
    temp_start = 0
    
    for i in range(1, len(numbers)):
        if current_sum < 0:
            current_sum = numbers[i]
            temp_start = i
        else:
            current_sum += numbers[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return max_sum, start, end


# Test cases
if __name__ == "__main__":
    # Example 1
    test1 = [-1, 5, -3, 9, -11]
    result1 = max_subarray_sum(test1)
    print(f"Input: {test1}")
    print(f"Output: {result1}")
    print(f"Expected: 11")
    print()
    
    # Example 2
    test2 = [9]
    result2 = max_subarray_sum(test2)
    print(f"Input: {test2}")
    print(f"Output: {result2}")
    print(f"Expected: 9")
    print()
    
    # Example 3
    test3 = [1, 2, 3, 4]
    result3 = max_subarray_sum(test3)
    print(f"Input: {test3}")
    print(f"Output: {result3}")
    print(f"Expected: 10")
    print()
    
    # Additional test with all negative numbers
    test4 = [-5, -2, -8, -1]
    result4 = max_subarray_sum(test4)
    print(f"Input: {test4}")
    print(f"Output: {result4}")
    print(f"Expected: -1 (least negative)")
    print()
    
    # Test with indices
    max_sum, start, end = max_subarray_sum_with_indices(test1)
    print(f"For {test1}:")
    print(f"Maximum sum: {max_sum}")
    print(f"Subarray: {test1[start:end+1]} (indices {start} to {end})")