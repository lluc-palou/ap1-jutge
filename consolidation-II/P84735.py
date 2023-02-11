from yogi import read

def print_number(a: int, b: int, i: int) -> None:
    """Prints the smallest natural number that is greater 
    than or equal to a and also a multiple of b."""

    x = a // b
    if (x * b != a):
        x += 1
    x *= b
    print('#', i, ' : ', x, sep = '', end = '\n')

def main() -> None:
    # Reads several cases.
    a = read(int)
    i = 1
    while a is not None:
        b = read(int)
        print_number(a, b, i)
        i += 1
        a = read(int)

if __name__ == '__main__':
    main()