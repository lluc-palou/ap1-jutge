from yogi import *
from typing import *

def dia_de_la_setmana(dia: int, mes: int, any: int) -> str:
    """Donada una data indica a quin dia de la setmana correspon."""
    m = mes - 2
    if m <= 0:
        m = m + 12
        a = any - 1
    else:
        m = mes
        a = any
    c = a // 100
    y = a % 100
    f = int(2.6 * m - 0.2) + dia + y + int(y / 4) + int(c / 4) - 2 * c
    
    # S'imprimeix el dia de la setmana.
    if f % 7 == 0:
        return 'Diumenge'
    elif f % 7 == 1:
        return 'Dilluns'
    elif f % 7 == 2:
        return 'Dimarts'
    elif f % 7 == 3:
        return 'Dimecres'
    elif f % 7 == 4:
        return 'Dijous'
    elif f % 7 == 5:
        return 'Divendres'
    elif f % 7 == 6:
        return 'Dissabte'

def main() -> None:
    # Es llegeixen el dia, el mes i l'any.
    dia = 1
    mes = 3
    any = 2000
    print(dia_de_la_setmana(dia, mes, any))

if __name__ == '__main__':
    main()

