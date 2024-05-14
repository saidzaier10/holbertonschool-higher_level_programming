#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """
    Replace an element in a list at a specific index and return a new list.

    Args:
        my_list (list): The original list.
        idx (int): The index of the element to be replaced.
        element: The new element to be inserted at the specified index.

    Returns:
        list: A new list with the element replaced at the specified index.
              If the index is negative or out of range, a copy of the original list is returned.
    """
    # Check if the index is negative or out of range of the list
    if idx < 0 or idx >= len(my_list):
        return my_list[:]  # Return a copy of the original list
    # Create a copy of the original list
    new_list = my_list[:]
    # Replace the element at the specified index in the copy of the list
    new_list[idx] = element
    return new_list


# Test the function
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = new_in_list(my_list, idx, new_element)
    print(new_list)
    print(my_list)
