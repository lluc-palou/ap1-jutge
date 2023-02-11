from re import I
from yogi import *

def factorial(n: int) -> int:
    """Calcula el factorial d'un nombre enter donat."""
    f = 1
    for i in range(2, n + 1):
        f = f * i
    return f

def main():
    # Es llegeix un nombre enter.
    n = read(int)
    print(factorial(n))

if __name__ == '__main__':
    main()