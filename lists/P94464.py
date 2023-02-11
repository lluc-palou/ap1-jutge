from yogi import read

def read_sequence() -> list[int]:
    """Returns a list with the sequence given 
    in the input."""

    List = []
    x = read(int)
    while x is not None:
        List.append(x)
        x = read(int)
    return List

def to_base_b(x: int, n: int, b: int) -> int:
    """Returns the given number with base b 
    representation."""

    if n >= b:
        to_base_b(x, n // b, b)
    return x * 10 + n % b

def most_frequent_digit(List: list[int]) -> int:
    """Returns the most frequent digit of 
    every element of the given List."""

    d = 0
    f = 0
    for i in range(len(List)):
        n = List[i]
        current_f = 0
        while n > 9:
            current_d = n % 10
            current_f += 1
            if current_f > f:
                d = current_d
            elif current_f == f:
                if current_d < d:
                    d = current_d
            n = n // 10
    return d

def main():
    # Reads the base and the given sequence.
    b = read(int)
    List = read_sequence()

    for i in range(len(List)):
        print(List[i])

    """
    # Converts the elements of the List to base b.
    for i in range(len(List)):
        List[i] = to_base_b(0, List[i], b)

    # Searches the most frequent digit.
    return most_frequent_digit(List)
    """

if __name__ == '__main__':
    main()