from yogi import read

def read_sequence(n: int) -> list[float]:
    """Returns a list with the sequence of n natural numbers given in 
    the input."""

    List = []

    for i in range(n):
        x = read(float)
        List.append(x)
    
    return List

def insert(v: list[float]) -> None:
    """Sorts the given vector in increasing order using the insertion sort algorithm."""

    n = len(v)
    for i in range(1, n):
        insert_into(v, i)

def insert_into(v: list[float], i: int) -> None:
    """Knowing that v[:i] is sorted, sorts L[:i+1]."""

    x = v[i]
    j = i
    while j > 0 and v[j - 1] > x: 
        v[j] = v[j - 1]
        j -= 1
    v[j] = x

def main() -> None:
    n = read(int)
    v = read_sequence(n)
    insert(v)
    print(v)

if __name__ == '__main__':
    main()