from yogi import *

def sum_divisors(x: int) -> int:
    """Retorna la suma dels divisors d'un nombre natural."""
    suma = 0
    i = 1
    while i * i < x:
        if x % i == 0:
            suma = suma + i
            suma = suma + x // i
        i = i + 1
    if i * i == x:
        suma = suma + i
    return suma

def main() -> None:
    # Es llegeix un nombre natural.
    x = read(int)
    print(sum_divisors(x))

if __name__ == '__main__':
    main()