from yogi import read

def generate_combinations(n: int) -> None:
    """Generates all possible sequences (2**n) in lexicographicall 
    order composed of combinations of (z) zeros and (o = n - k) ones."""

    generate_combinations_rec(n, [0 for _ in range(n)], 0, n)

def generate_combinations_rec(n: int, L: list[int], i: int, z: int) -> None:
    """Writes all possible sequences of lenght n, starting with L,
    composed of combinations of (z) zeros and (o = n - k) ones, where 
    the next element of the sequence to be defined is at the position i."""

    # Pruning (when we can add more elements to a correct sequence).
    if z >= 0 and z <= n - i:
        if i == n:
            write_sequence(L)
        
        else:
            # Concatenates a zero to the previous sequence.
            L[i] = 0
            generate_combinations_rec(n, L, i + 1, z - 1)

            # Concatenates a one to the previous sequence.
            L[i] = 1
            generate_combinations_rec(n, L, i + 1, z - 1)

def write_sequence(L: list[int]) -> None:
    """Writes the given generated sequence."""

    # Converts the integers to text using ' ' as a separator.
    print(' '.join([str(x) for x in L]))

def main() -> None:
    # Reads a natural number.
    n = read(int)
    generate_combinations(n)

if __name__ == '__main__':
    main()