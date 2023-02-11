from yogi import read

def read_sequence(n: int) -> list[int]:
    """Returns a list with the sequence of n natural numbers given in 
    the input."""

    List = []

    for i in range(n):
        x = read(int)
        List.append(x)
    
    return List

def print_reverse(List: list[int]) -> None:
    """Prints the given sequence in reverse order."""

    lenght = len(List)

    if lenght == 0:
        print(end = '\n')

    else:
        for i in range(lenght - 1):
            print(List[-1], end = ' ')
            List.pop()
        print(List[-1], end = '\n')

def main() -> None:
    # Reads several sequences of natural numbers.
    n = read(int)
    while n is not None:
        List = read_sequence(n)
        print_reverse(List)
        n = read(int)

if __name__ == '__main__':
    main()