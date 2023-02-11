from yogi import *

def number_of_digits(n: int) -> int:
    """Retorna el nombre de digits que té un nombre enter donat."""
    d = 1
    while n > 9:
        d = d + 1
        n = n // 10
    return d

def main() -> None:
    # Es llegeix un nombre enter.
    n = read(int)
    print(number_of_digits(n))

if __name__ == '__main__':
    main()