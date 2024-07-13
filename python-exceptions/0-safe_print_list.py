#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    printed_elements = 0

    try:
        # Attempt to count the elements in my_list without using len()
        for _ in my_list:
            count += 1
    except TypeError:
        # If my_list is not iterable (which should not happen here due to default value), return 0
        return 0
    
    try:
        # Print up to x elements
        for i in range(x):
            print(my_list[i], end=' ')
            printed_elements += 1
    except IndexError:
        # IndexError will be caught if x is greater than the number of elements in my_list
        pass
    
    print()  # To move to the next line after printing all elements
    return printed_elements

# Example usage:
print(safe_print_list([1, 2, 3, 4], 6))  # This will print "1 2 3 4" and return 4
print(safe_print_list(['a', 'b', 'c'], 2))  # This will print "a b" and return 2
print(safe_print_list([], 3))  # This will print nothing and return 0

