from yogi import read

def read_sequence(n: int) -> list[int]:
    """Reads a sequence of natural numbers"""

    List: list[int] = [0]*1001

    for i in range(n):
        x = read(int)
        List[x%10000] += 1 

    return List

def print_frequencies(S: list[int]) -> None:
    """Prints the frequencies in which the elements of the sequence appear in it."""

    for i in range(1001):
        if S[i] != 0:
            print(i + 1000000000, ' : ', S[i], sep = '', end = '\n')

def main() -> None:
    # Reads the number of elements in the sequence.
    n = read(int)
    S = read_sequence(n)
    print_frequencies(S)
    
if __name__ == '__main__':
    main()