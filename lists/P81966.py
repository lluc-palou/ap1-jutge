from yogi import read

def position(x: float, v: list[float], left: int, right: int) -> int:
    """Returns the position of the element x in the subvector v[left..right], 
    in case that x does not belong to v or left > right returns -1."""

    # Precondition: the vector has to be already sorted increasingly.
    if left > right:
        return -1
    else:
        # Index of the middle element.
        middle = (left + right) // 2

        if x < v[middle]:
            return position(x, v, left, middle - 1)
        elif x > v[middle]:
            return position(x, v, middle + 1, right)
        else:
            return middle

def main() -> None:
    # Reads the element x.
    x = 5.0
    # Reads a list of elements, a vector.
    v = [0.4, 1.0, 2.1, 3.7, 4.3, 5.0, 6.7, 7.5, 8.2, 9.5] 
    print(position(x, v, 0, len(v) - 1))

if __name__ == '__main__':
    main()