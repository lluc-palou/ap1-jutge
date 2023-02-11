from yogi import *
from typing import *

def semiprimalitat(n: int) -> Optional[tuple[int, int]]:
    """Donat un nombre natural retorna dos primers tals que el seu producte
    dona aquest, altrament retorna None."""
    i = 1
    while i * i <= n:
        if n % i == 0:
            if es_primer(i) and es_primer(n // i):
                return (i, n // i)
        i = i + 1
    return None
    
def es_primer(n: int) -> bool:
    """Donat un nombre natural indica si aquest és primer."""
    if n <= 1:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 1
    return True

def main() -> None:
    # Es llegeix un nombre natural.
    n = read(int)
    print(semiprimalitat(n))

if __name__ == '__main__':
    main()