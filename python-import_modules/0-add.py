#!/usr/bin/python3
# Ensure this code runs only when the script is executed directly, not when imported
if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2
    result = add(a, b)
    print(f"{a} + {b} = {result}")

