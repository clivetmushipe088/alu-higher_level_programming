#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # Initialize counters
    count = 0  # To count the number of elements in my_list
    printed_elements = 0  # To count how many elements are printed
    
    # Determine the number of elements in my_list
    try:
        for _ in my_list:
            count += 1
    except TypeError:
        # If my_list is not iterable, return 0
        return 0
    
    # Attempt to print up to x elements from my_list
    for i in range(x):
        try:
            # Attempt to access and print the ith element
            print(my_list[i], end=' ')
            printed_elements += 1
        except IndexError:
            # If an IndexError occurs, break the loop
            break
    
    print()  # Move to a new line after printing
    return printed_elements

# Example usage:
print(safe_print_list([1, 2, 3, 4], 6))  # This will print "1 2 3 4" and return 4
print(safe_print_list(['a', 'b', 'c'], 2))  # This will print "a b" and return 2
print(safe_print_list([], 3))  # This will print nothing and return 0

