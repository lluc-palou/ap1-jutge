from yogi import read

def read_sequence(x_i) -> None:
    """Prints the content of the x_i element of the given sequence
    if it exist, otherwise prints incorrect position."""

    # Reads the sequence of natural numbers ended with -1.
    index = 1
    element = None
    x_n = read(int)
    while x_n >= 0:
        if index == x_i:
            element = x_n
        index += 1
        x_n = read(int)
        
    # Output.
    if element is not None:
        print('At the position ', x_i, ' there is a(n) ', element, '.', sep = '', end = '\n')
    else:
        print('Incorrect position.', sep = '', end = '\n')

def main() -> None:
    # Reads the x_i number.
    x_i = read(int)

    # Reads the several cases.
    while x_i is not None:
        read_sequence(x_i)
        x_i = read(int)

if __name__ == '__main__':
    main()