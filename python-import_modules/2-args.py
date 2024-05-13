#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Récupérer les arguments depuis sys.argv
    argv = sys.argv[1:]  # Ignorer le nom du script lui-même (sys.argv[0])
    num_args = len(argv)

    # Imprimer le nombre d'arguments
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(num_args))

    # Imprimer chaque argument avec sa position
    for index, argument in enumerate(argv, start=1):
        print("{:d}: {}".format(index, argument))
