# Function to calculate m-lucky number
def lucky_number(n, a):
    res = [-1] * n  # Initialize the result list with -1
    
    # Create a dictionary to store the minimum index for each value
    min_index = {}
    
    # Iterate through the array
    for i, num in enumerate(a):
        # Update the minimum index for the current value
        if num in min_index:
            min_index[num] = min(min_index[num], i)
        else:
            min_index[num] = i
        
        # Iterate through each possible length m
        for m in range(1, n + 1):
            # Check if the current value has occurred in all subarrays of length m
            if num in min_index and min_index[num] <= i - m + 1:
                # Update the m-lucky number if the condition is met
                res[m - 1] = num
    
    return res

# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the number of elements and the array
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Calculate the m-lucky numbers
    result = lucky_number(n, arr)
    
    # Print the result for the current test case
    print(*result)
