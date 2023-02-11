from yogi import *

def es_primer(n: int) -> bool:
    """Donat un nombre enter ens indica si aquest és primer."""
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

    # Imprimeix tots els divisors primers del nombre.
    d = 1
    while d * d <= n:
        if n % d == 0:
            n = n // d
            if es_primer(d):
                print(d)
            else:
                d = d + 1
        else:
            d = d + 1
    if n > 0 and es_primer(n):
        print(n)


if __name__ == '__main__':
    main()