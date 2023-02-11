from yogi import read

def generate_permutations(n: int) -> None:
    """Generates all the sequences of permutations in lexicographicall order, 
    that contain the numbers from 1 to (n)."""

    L = [0 for _ in range(n)]
    used = [False for _ in range(n + 1)]
    generate_permutations_rec(n, L, 0, used)

def generate_permutations_rec(n: int, L: list[int], i: int, used: list[bool]) -> None:
    """Writes all the sequences of permutations containing the numbers from 1 to n, starting with L, 
    where the next element of the sequence to be defined is at the position i."""

    if i == n:
        write_sequence(L)
    
    else:
        for x in range(1, n + 1):
            # The sequence doesn't contain repeated elements.
            if not used[x]:
                L[i] = x
                used[x] = True
                generate_permutations_rec(n, L, i + 1, used)
                used[x] = False

def write_sequence(L: list[int]) -> None:
    """Writes the given generated sequence."""

    print('(', ','.join([str(x) for x in L]), ')', sep = '', end = '\n')

def main() -> None:
    # Reads a natural number (n : n > 0).
    n = read(int)
    generate_permutations(n)

if __name__ == '__main__':
    main()