#!/bin/bash
# Tady nic není.
# Robota spustis tak, ze napises ./robot.sh
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



















clear
echo
echo
echo "Dobry. Den. Co. Pro. Vas. Mohu. Zanalyzovat?"
echo

# Prompt user for single letter
echo -n "Zmacknete prvni pismeno predmetu, ktery chcete analyzovat. (napr. L pro lopatu, K pro konec): "
read -n1 choice
echo
echo

case "${choice,,}" in  # ,,: lowercase
  k)
    echo "Analyzuji... Na nozi nejsou zadne prokazatelne otisky"
    ;;
  o)
    echo "Lopata je pouze priklad. Spuste znovu a zadejte prvni pismenko Vaseho predmetu"
    ;;
  p)
    echo "Analyzuji... Na pacidlu je otisk prstu doktora Fialy"
    ;;
  l)
    echo "Analyzuji... Toto je otisk prstu doktora Fialy"
    ;;
  n)
    echo "Konec programu."
    ;;
  *)
    echo "Neznama volba."
    ;;
esac
