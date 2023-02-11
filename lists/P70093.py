def merge(L1: list[float], L2: list[float]) -> list[float]:
    """Given two sorted lists returns another sorted list with elements from both."""

    n1, n2 = len(L1), len(L2)
    i1, i2 = 0, 0
    R: list[float] = []

    while i1 < n1 and i2 < n2:
        if L1[i1] <= L2[i2]:
            R.append(L1[i1])
            i1 += 1
        else:
            R.append(L2[i2])
            i2 += 1
    R.extend(L1[i1:])
    R.extend(L2[i2:])

    return R

def main() -> None:
    L1 = [2.4, 3.2, 5.9]
    L2 = [3.2, 5.7, 5.8, 7.4]
    L = merge(L1, L2)
    print(L)

if __name__ == '__main__':
    main()