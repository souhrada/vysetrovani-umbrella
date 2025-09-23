#!/usr/bin/env python3

# Tady je pouze kod.
# Robota spustis tak, ze napises python3 robot.py
# do prikazoveho radku a zmacknes enter





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
    print("Dobry. Den. Co. Pro. Vas. Mohu. Zanalyzovat?")
    print()
    choice = input(
        "Zmacknete prvni pismeno predmetu, ktery chcete analyzovat.\n"
        "Napr. pro lopatu zmacknete L. Pro konec stisknete K: "
    ).strip().lower()

    if choice == "k":
        clear()
        print("\nAnalyzuji... Na nozi nejsou zadne prokazatelne otisky\n")
    elif choice == "o":
        clear()
        print("\nLopata je pouze priklad. Spuste znovu a zadejte prvni pismenko Vaseho predmetu\n")
    elif choice == "p":
        clear()
        print("\nAnalyzuji... Na pacidlu je otisk prstu doktora Fialy\n")
    elif choice == "l":
        clear()
        print("\nAnalyzuji... Toto je otisk prstu doktora Fialy\n")
    elif choice == "n":
        clear()
        print("\nKonec programu.\n")
    else:
        clear()
        print("\nNeznama volba.\n")

if __name__ == "__main__":
    main()
