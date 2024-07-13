#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0  # To count the number of elements in my_list
    printed_elements = 0  # To count how many elements are actually printed
    
    # Determine the number of elements in 
    try:
        for _ in my_list:
            count += 1
    except TypeError:
        return 0  # In case my_list is not iterable
    
    # Print up to x elements
    for i in range(x):
        try:
            print(my_list[i], end='')
            printed_elements += 1
        except IndexError:
            break  # Stop printing if there are no more elements to print
    
    print()  # Move to a new line after printing all elements
    return printed_elements

# Test cases
print(safe_print_list([1, 2, 3, 4], 4))  # Expected output: 1234\n (4)
print(safe_print_list([1, 2, 3, 4], 2))  # Expected output: 12\n (2)
print(safe_print_list([1, 2, 3, 4], 0))  # Expected output: \n (0)
print(safe_print_list([], 0))             # Expected output: \n (0)
print(safe_print_list([1, 2, 3, 4], 5))  # Expected output: 1234\n (4)
print(safe_print_list([1, 2, 3, 4], 14)) # Expected output: 1234\n (4)

