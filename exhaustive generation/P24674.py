from yogi import read

def generate_permutations(n: int, W: list[str]) -> None:
    """Generates all the possible sequences of permutations of lenght (n),
    that contain the given words."""

    S: list[str] = ["." for _ in range(n)]
    used = [False for _ in range(n)]
    generate_permutations_rec(n, W, S, 0, used)

def generate_permutations_rec(n: int, W: list[str], S: list[str], i: int, used: list[bool]) -> None:
    """Writes all the possible sequences of permutations of lenght (n), 
    that contain the given words, starting with L, where the next element of the
    sequence to be defined is at the position i."""

    if i == n:
        write_sequence(S)

    else:
        for x in range(len(W)):
            if not used[x]:
                S[i] = W[x]
                used[x] = True
                generate_permutations_rec(n, W, S, i + 1, used)
                used[x] = False

def write_sequence(S: list[str]) -> None:
    """Writes the given generated sequence."""

    print('(', ','.join(S), ')', sep = '', end = '\n')
    
def main() -> None:
    # Reads a natural number (n : n > 0), folloed by (n) words.
    n = read(int)
    W: list[str] = []

    for _ in range(n):
        w = read(str)
        W.append(w)

    generate_permutations(n, W)

if __name__ == '__main__':
    main()