#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    # Parcours la liste en ordre inverse
    for num in reversed(my_list):
        print("{:d}".format(num))


# Test de la fonction
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_reversed_list_integer(my_list)
