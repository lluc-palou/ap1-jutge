from yogi import read

def print_rombus(n: int) -> None:
    """Prints a rombus with 2n - 1 lines, given the size n."""

    # Prints from the first row to the (n - 1)-th.
    for i in range(1, n):
        # Row inside spaces.
        for j in range(0, n - i):
            print(' ', sep = '', end = '')
        # Row stars.
        for k in range(0, 2*i - 1):
            print('*', sep = '', end = '')
        print(end = '\n')
    
    # Prints the n-th row.
    for j in range(0, 2*n - 1):
        # Row stars.
        print('*', sep = '', end = '')
    print(end = '\n')

    # Prints from the (n + 1)-th row to the (2n - 1)-th.
    for i in range(n + 1, 2*n):
        # Row inside spaces.
        for j in range(0, i - n):
            print(' ', sep = '', end = '')
        # Row stars.
        for k in range(0, 4*n - 2*i - 1):
            print('*', sep = '', end = '')
        print(end = '\n')

def main() -> None:
    # Reads the size of the rombus.
    n = read(int)
    print_rombus(n)

if __name__ == '__main__':
    main()