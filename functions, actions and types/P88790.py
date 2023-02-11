from yogi import *

def gcd(a: int, b: int) -> int:
    """Retorna el màxim comú divisor de dos nombres enters
    donats emprant el mètode ràpid de l'algorísme d'Euclides."""
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
    
def main():
    # Es llegeixen dos nombres enters.
    a = read(int)
    b = read(int)
    print(gcd(a, b))

if __name__ == '__main__':
    main()