#!/usr/bin/env python3

# Tady je pouze kod.
# Robota spustis tak, ze napises python3 robot.py
# do prikazoveho radku a zmacknes enter
#
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
##
#
#
#
#
#
#
#
#
#

# ⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀
# ⠀⠀⠀⢀⣿⣿⣿⣿⡿⠛⢿⡿⠛⢻⣿⣿⣿⣿⡀⠀⠀⠀
# ⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⢸⣷⣶⣾⣿⣿⣿⣿⡇⠀⠀⠀
# ⠀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠈⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀
# ⠀⢀⣤⣀⣾⣿⣿⣿⠟⠛⠛⠛⠛⠻⣿⣿⣿⣷⣀⣤⡀⠀
# ⠀⢸⣿⣿⣿⣿⣿⣿⣤⣤⣤⣤⣤⣤⣿⣿⣿⣿⣿⣿⡇⠀
# ⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
# ⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
# ⠀⢸⣿⡟⢿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⡿⢻⣿⡇⠀
# ⠀⢸⣿⡇⠈⠙⠛⢛⣿⣿⣤⣤⣿⣿⡛⠛⠋⠁⢸⣿⡇⠀
# ⣤⣼⣿⣧⣤⡀⠀⠙⠛⠛⠛⠛⠛⠛⠋⠀⢀⣤⣼⣿⣧⣤
# ⠛⠛⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠛⠛


import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    clear()
    print()
    print()
    print("Dobrý. Den. Co. Pro. Vás. Mohu. Zanalyzovat?")
    print()
    choice = (
        input(
            "Jaký předmět má být zanalyzován?.\n"
            "Napiš název předmětu, který chceš vyšetřit. Pro konec stiskni K: "
        )
        .strip()
        .lower()
    )

    if choice == "nuz" or choice == "nůž":
        clear()
        print("\nAnalyzuji... Na noži nejsou žádné prokazatelné otisky\n")
    elif choice == "pacidlo" or choice == "páčidlo":
        clear()
        print("\nAnalyzuji... Na páčidlu je otisk prstu doktora Kroupy\n")
    elif choice == "otisk":
        clear()
        print("\nAnalyzuji... Toto je otisk prstu doktora Kroupy\n")
    elif choice == "k":
        clear()
        print("\nKonec programu.\n")
    else:
        clear()
        print(f"\n{choice} není ničím speciální.\n")


if __name__ == "__main__":
    main()

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


# ⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀
# ⠀⠀⠀⢀⣿⣿⣿⣿⡿⠛⢿⡿⠛⢻⣿⣿⣿⣿⡀⠀⠀⠀
# ⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⢸⣷⣶⣾⣿⣿⣿⣿⡇⠀⠀⠀
# ⠀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠈⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀
# ⠀⢀⣤⣀⣾⣿⣿⣿⠟⠛⠛⠛⠛⠻⣿⣿⣿⣷⣀⣤⡀⠀
# ⠀⢸⣿⣿⣿⣿⣿⣿⣤⣤⣤⣤⣤⣤⣿⣿⣿⣿⣿⣿⡇⠀
# ⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
# ⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
# ⠀⢸⣿⡟⢿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⡿⢻⣿⡇⠀
# ⠀⢸⣿⡇⠈⠙⠛⢛⣿⣿⣤⣤⣿⣿⡛⠛⠋⠁⢸⣿⡇⠀
# ⣤⣼⣿⣧⣤⡀⠀⠙⠛⠛⠛⠛⠛⠛⠋⠀⢀⣤⣼⣿⣧⣤
# ⠛⠛⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠛⠛
