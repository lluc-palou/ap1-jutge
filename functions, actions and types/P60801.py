from yogi import *

def escriure_factors_primers(n: int) -> None:
    """Imprimeix els factors primers del nombre natual ordenats de petit a gran."""
    if n <= 1:
        print()

    elif es_primer(n):
        print(n)

    else:
        primer_factor = True
        d = 2
        while n != 1:
            if n % d == 0:
                if primer_factor:
                    primer_factor = False
                    n = n // d
                    ultim_factor = d
                else:
                    n = n // d
                    if es_primer(d):
                        if d > ultim_factor:
                            print(ultim_factor, end = ',')
                            ultim_factor = d
                    else:
                        d = d + 1
            else:
                d = d + 1
        print(ultim_factor)
        

def es_primer(n: int) -> bool:
    """Indica si el nombre enter proporcionat és primer."""
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
    x = read(int)
    escriure_factors_primers(x)

if __name__ == '__main__':
    main()