from yogi import *

def gcd4(a: int, b: int, c: int, d: int) -> int:
    """Retorna el màxim comú divisor de 4 nombres enters
    donats emprant el mètode ràpid de l'algorísme d'Euclides."""
    return gcd(gcd(a, b), gcd(c, d))

def gcd(a: int, b: int) -> int:
    """Retorna el màxim comú divisor de dos nombres enters
    donats emprant el mètode ràpid de l'algorísme d'Euclides."""
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def main() -> None:
    # Es legeixen 4 nombres enters.
    a = read(int)
    b = read(int)
    c = read(int)
    d = read(int)
    print(gcd4(a, b, c, d))

if __name__ == '__main__':
    main()