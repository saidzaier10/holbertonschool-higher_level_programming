#!/usr/bin/python3

if __name__ == "__main__":
    # Importer le module compilé hidden_4
    import hidden_4

    # Obtenir la liste de tous les noms dans hidden_4
    names = dir(hidden_4)

    # Trier et filtrer les noms qui ne commencent pas par '__'
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
