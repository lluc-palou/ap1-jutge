from yogi import read

def read_sequence(n: int) -> list[int]:
    """Returns a list with the sequence of n natural numbers given in 
    the input."""

    List = []

    for i in range(n):
        x = read(int)
        List.append(x)
    
    return List

def ocurrences(List: list[int], element: int) -> int:
    """Returns the number of ocurrences of a certain event. In this case,
    when an element of the list is equal to the last one."""

    counter = 0

    for i in range(len(List) - 1):
        if List[i] == element:
            counter += 1
    
    return counter

def main() -> None:
    # Reads a natural number, corresponding to the lenght of the natural 
    # number sequence.
    n = read(int)
    List = read_sequence(n)
    print(ocurrences(List, List[-1]), sep = '', end = '\n')

if __name__ == '__main__':
    main()