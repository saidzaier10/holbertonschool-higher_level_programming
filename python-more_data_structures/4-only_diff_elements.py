#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """
    Return a set containing the elements that are present in either set_1 or set_2, but not both.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A set containing the elements that are present in either set_1 or set_2, but not both.
    """
    return set_1.symmetric_difference(set_2)
