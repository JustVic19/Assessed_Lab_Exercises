def calculate_average(numbers):
    """
    This function calculates the average of a list of numbers using a for loop.

    Parameters:
    ----------
    numbers : list
        A list of numerical values (int or float).

    Returns:
    -------
    float:
        The average of the numbers in the list. If the list is empty, returns None.

    Example:
    --------
    calculate_average([10, 20, 30, 40, 50])  # Output: 30.0
    """
    
    if not numbers:
        return None

    total = 0
    for number in numbers:
        total += number

    average = total / len(numbers)
    return average

# # Example usage
numbers = [34, 70, 45, 88, 134]
print("The average is:", calculate_average(numbers))  # Expected output: The average is: 30.0
