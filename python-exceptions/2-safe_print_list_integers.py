#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Skip if the current element is not an integer
            continue
        except IndexError:
            # If x is greater than the length of the list, break out of the loop
            break
    print()  # Print a newline at the end
    return count
