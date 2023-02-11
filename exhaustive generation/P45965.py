from yogi import read

def generate_combinations(n: int, o: int) -> None:
    """Generates all the possible binary sequences (2**n) in lexicograhpicall order,
    composed of combinations of (z = n - o) zeros and (o) ones."""

    generate_combinations_rec(n, [0 for _ in range(n)], 0, o)

def generate_combinations_rec(n: int, L: list[int], i: int, o: int) -> None:
    """Writes all the sequences of lenght (n), starting with L, composed of combinations
    of (z = n - o) zeros and (o) ones, where the next elementof the sequence to be defined
    is at the position i.
    """

    # Pruning.
    if o >= 0 and o <= n - i:
        if i == n:
            write_sequence(L)
        
        else:
            L[i] = 0
            generate_combinations_rec(n, L, i + 1, o)
            L[i] = 1
            generate_combinations_rec(n, L, i + 1, o - 1)

def write_sequence(L: list[int]) -> None:
    """Writes the given generated sequence."""

    print(' '.join([str(x) for x in L]))

def main() -> None:
    # Reads the lenght of the sequences and the number of ones of each.
    n = read(int)
    o = read(int)
    generate_combinations(n, o)

if __name__ == '__main__':
    main()