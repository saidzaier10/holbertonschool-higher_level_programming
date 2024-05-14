#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Pad the tuples with 0 if they are smaller than 2
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    
    # Take the first 2 elements of each tuple and add them
    sum_a = tuple_a[0] + tuple_b[0]
    sum_b = tuple_a[1] + tuple_b[1]
    
    # Return the resulting tuple
    return (sum_a, sum_b)