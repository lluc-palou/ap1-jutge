from yogi import read

def print_bars(n: int) -> None:
    """Prints n^(n) - 1 bars following the corresponding pattern."""
    if n == 1:
        print('*', sep = '', end = '\n')
    else:
        print_bars(n - 1)
        print_bars(n - 1)
        for i in range(n):
            print('*', sep = '', end = '')
        print(end = '\n')

def main() -> None:
    # Reads a natural number.
    n = read(int)

    # Prints 2^(n) - 1 bars.
    print_bars(n)

if __name__ == '__main__':
    main()