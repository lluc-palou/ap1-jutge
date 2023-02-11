from yogi import read

def position_maximum(v: list[float], m: int) -> int:
    """Returns the position of the maximum element in the vector v."""

    p = 0
    max = v[0]
    for i in range(1, m + 1):
        if v[i] > v[p]:
            p = i
            max = v[i]
    return p

def main() -> None:
    v = [1.3, 2.4, 5.8, 4.6, 8.3]
    print(position_maximum(v, 3))

if __name__ == '__main__':
    main()