from yogi import read

def factorial(n: int) -> int:
    """Calcula el factorial del nombre natural introduit."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main() -> None:
    # Es llegeix un nombre natural.
    n = read(int)
    print(factorial(n))

if __name__ == '__main__':
    main()