from yogi import *
from typing import *

def factor_mes_petit(n: int) -> Optional[int]:
    """Retorna el factor més petit del nombre natural quan aquest
    no és primer, en cas contrari, retorna None."""
    if es_primer(n):
        return None

    i = 1
    while i * i < n:
        if n % i == 0:
            if es_primer(i):
                return i
        i = i + 1

    if i * i == n:
        if es_primer(i):
            return i

def es_primer(n: int) -> bool:
    """Indica si el nombre natural proporcionat és primer."""
    if n <= 1:
        return False

    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 1

    return True

def main() -> None:
    # Es llegeix un nombre enter.
    n = read(int)
    print(factor_mes_petit(n))

if __name__ == '__main__':
    main()