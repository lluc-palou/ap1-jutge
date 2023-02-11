from yogi import read

def es_primer(n: int) -> bool:
    """Indica si el nombre introduit és primer."""

    if n <= 1:
        return False
    else:
        d = 2
        while d * d <= n:
            if n % d == 0:
                return False
            d = d + 1
        return True

def suma_dels_digits(n: int) -> int:
    """Retorna la suma dels dígits d'un nombre donat."""

    if n < 10:
        return n
    else:
        return n % 10 + suma_dels_digits(n // 10)

def is_perfect_prime(n: int) -> bool:
    """Indica si el nombre introduit és un primer perfecte, és a dir,
    que la suma dels seus digits en tot moment és un nombre primer."""

    if es_primer(n):
        if n < 10 and es_primer(n):
            return True
        elif es_primer(suma_dels_digits(n)):
            return is_perfect_prime(suma_dels_digits(n))
        else:
            return False
    else:
        return False
'''
def main() -> None:
    # Es llegeix un nombre natural.
    n = read(int)
    if is_perfect_prime(n):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
'''
