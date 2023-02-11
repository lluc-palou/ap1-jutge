from yogi import read

def lenght_longest_cycle(Permutation: list[int]) -> int:
    """Returns the lenght of the longest cycle of the sequence of permutations."""
    max_lenght = 0

    for i in range(len(Permutation)):
        start_cycle = Permutation[i]
        current_element = Permutation[start_cycle - 1]
        current_lenght = 1

        if start_cycle != current_element:
            while start_cycle != current_element:
                current_element = Permutation[current_element - 1]
                current_lenght += 1

            if current_lenght > max_lenght:
                max_lenght = current_lenght
            
        elif max_lenght < current_lenght:
            max_lenght = current_lenght

    return max_lenght
    
def main() -> None:
    # Reads several cases of lenght (n), followed by a sequence.
    n = read(int)
    
    while n is not None:
        Permutation: list[int] = []

        for _ in range(n):
            x = read(int)
            Permutation.append(x)

        print(lenght_longest_cycle(Permutation), end = '\n')

if __name__ == '__main__':
    main()