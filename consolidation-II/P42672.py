from yogi import read

def binary_mix(a: int, b: int) -> None:
    """Prints the binary mix of the two given numbers."""

    if a >= 2:
        binary_mix(a // 2, b // 2)
    print(a % 2, sep = '', end='')
    print(b % 2, sep = '', end='')

def main() -> None:
    # Reads several cases.
    a = read(int)
    while a is not None:
        b = read(int)
        binary_mix(a, b)
        print(end = '\n')
        a = read(int)

if __name__ == '__main__':
    main()