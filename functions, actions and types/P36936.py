from yogi import *

def es_primer(n: int) -> bool:
    """Indica si un nombre natural és primer."""
    if n <= 1:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 1
    return True
"""
def main() -> None:
    # Es llegeix un nombre enter.
    n = read(int)

    if es_primer(n):
        print('Si')
    else:
        print('No')

if __name__ == '__main__':
    main()
"""