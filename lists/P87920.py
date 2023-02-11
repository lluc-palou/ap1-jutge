from yogi import read

def sum_of_the_rest(sum: int, List: list[int]) -> int:
    """Tells if the sum of the remaining elements of 
    the list is equal to the ith element of the list."""

    for i in range(len(List)):
        if List[i] == sum - List[i]:
            return True
    return False

def parse_sequence(n: int) -> bool:
    """Analyses the given sequence and tells if 
    any number is equal to the sum of the rest."""

    List = []
    sum = 0

    # Reads the current sequence and computes the 
    # sequential sum since the ith element readed.
    for i in range(n):
        x = read(int)
        sum += x
        List.append(x)
    
    # Property check:
    if sum_of_the_rest(sum, List):
        return True
    else:
        return False

def main() -> None:
    # Reads several sequences of integer numbers.
    n = read(int)
    while n is not None:
        if parse_sequence(n):
            print('YES', end = '\n')
        else:
            print('NO', end = '\n')
        n = read(int)
        
if __name__ == '__main__':
    main()