from yogi import read

def gcd(a: int, b: int) -> int:
    """Calcula el màxim comú divisor emprant la versió ràpida de l'algorísme d'Euclides."""
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        if a > b:
            return gcd(a % b, b)
        else:
            return gcd(a, b % a)
            
def main() -> None:
    # Es llegeixen dos nombres enters.
    a = read(int)
    b = read(int)
    print(gcd(a, b))

if __name__ == '__main__':
    main()