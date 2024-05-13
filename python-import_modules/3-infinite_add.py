#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Récupérer tous les arguments, sauf le nom du script (argv[0])
    argv = sys.argv[1:]

    # Initialiser la somme totale à 0
    total = 0

    # Parcourir chaque argument et l'ajouter après l'avoir converti en entier
    for arg in argv:
        total += int(arg)

    # Imprimer la somme totale
    print("{:d}".format(total))
