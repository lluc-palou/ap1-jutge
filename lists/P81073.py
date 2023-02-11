def selsort(v: list[float]) -> None:
    """Sorts the given vector in increasing order using the selection sort algorithm."""

    n = len(v)

    for i in range(n - 1):
        # Finds the minimum element in the vector and swaps it with the i-th one.
        p = minimal_position(v, i)
        v[i], v[p] = v[p], v[i]

def minimal_position(v: list[float], i: int) -> int:
    """Returns the position of the minimal element between the i-th and the last one."""

    p = i

    for j in range(i + 1, len(v)):
        if v[j] < v[p]:
            p = j

    return p

def main() -> None:
    v = [2.4, 6.7, 1.2, 9.3]
    selsort(v)
    print(v)

if __name__ == '__main__':
    main()
