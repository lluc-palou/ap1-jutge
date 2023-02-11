from yogi import read

def sum_of_fractions(a: int, b: int, k: int) -> float:
    """Computes the sum of fractions given the triple of numbers."""
    sum = 0.0
    i = 0
    while a + i * k <= b:
        sum += 1 / (a + i * k)
        i += 1
    return sum

def main() -> None:
    # Reads the sequence of triples of natural numbers.
    a = read(int)
    while a is not None:
        b = read(int)
        k = read(int)
        print("{:.4f}".format(sum_of_fractions(a, b, k)), sep = '', end = '\n')
        a = read(int)

if __name__ == '__main__':
    main()