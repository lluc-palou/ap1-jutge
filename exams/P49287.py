from yogi import read

def generate_combinations(n: int, c: str) -> None:
    """Generates all the possible sequences of combinations of lenght (n),
    that start with the character (c) and every character is followed by 
    another one that's 2 units greatter that the first as a minimum bound."""

    L = ["." for _ in range(n)]
    L[0] = c
    generate_combinations_rec(n, L, 1)

def generate_combinations_rec(n: int, L: list[str], i: int) -> None:
    """Writes all the possible sequences of combinations of lenght (n),
    that start with L, where the next element of the sequence to be defined
    is at the position i."""

    if i <= n:
        if i == n:
            write_sequence(L)
            
        else:
            if ord(L[i - 1]) + 2 <= ord('z'):
                L[i] = chr(ord(L[i - 1]) + 2)
                generate_combinations_rec(n, L, i + 1)
            if ord(L[i - 1]) + 3 <= ord('z'):
                L[i] = chr(ord(L[i - 1]) + 3)
                generate_combinations_rec(n, L, i + 1)
            if ord(L[i - 1]) + 4 <= ord('z'):
                L[i] = chr(ord(L[i - 1]) + 4)
                generate_combinations_rec(n, L, i + 1)

def write_sequence(L: list[str]) -> None:
    """Writes the given generated sequence."""

    print(''.join(L))

def main() -> None:
    # Reads a natural number (n : n >= 1) and a character (c).
    n = read(int)
    c = read(str)
    generate_combinations(n, c)

if __name__ == '__main__':
    main()