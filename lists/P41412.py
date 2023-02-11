def insertion_sort(v: list[float]) -> None:
    """Sorts the given vector in increasing order using the insertion sort algorithm."""

    n = len(v)
    for i in range(1, n):
        insert(v, i)

def insert(v: list[float], i: int) -> None:
    """Knowing that v[:i] is sorted, sorts L[:i+1]."""

    x = v[i]
    j = i
    while j > 0 and v[j - 1] > x: 
        v[j] = v[j - 1]
        j -= 1
    v[j] = x

def main() -> None:
    v = [3.5, 1.2, 9.2, 6.8, 9.5, 3.4, 5.7]
    insertion_sort(v)
    print(v)

if __name__ == '__main__':
    main()