from yogi import *

def max2(a: int, b: int) -> int:
    """Retorna el màxim de dos nombres enters donats."""
    if a > b:
        return a
    else:
        return b

def main():
    # Es llegiexen dos nombres enters.
    a = read(int)
    b = read(int)
    print(max2(a, b))


if __name__ == '__main__':
    main()