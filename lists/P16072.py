def intersection(v1: list[float], v2: list[float]) -> list[float]:
    """Given two sorted lists returns another sorted list with the
    elements of the intersection from both, without repetitions."""

    v: list[float] = []
    n1, n2 = len(v1), len(v2)
    i1, i2 = 0, 0
    last_intersection_element = 0.0

    while i1 < n1 and i2 < n2:
        if v1[i1] < v2[i2]:
            i1 += 1

        elif v1[i1] == v2[i2] and last_intersection_element != v1[i1]:
            v.append(v1[i1])
            last_intersection_element = v1[i1]
            i1 += 1
            i2 += 1

        else:
            i2 += 1

    return v

def main() -> None:
    v1 = [-5.6, -5.6, 0.0, 0.0, 0.0, 0.0, 0.0, 2.4, 3.2, 3.2 , 5.8, 5.9, 7.3, 7.4, 7.4, 7.4]
    v2 = [-5.6, -5.6,  -2.4, 0.0, 0.0, 0.0, 3.2, 5.7, 5.8, 5.9, 7.4, 7.4]
    v = intersection(v1, v2)
    print(v)

if __name__ == '__main__':
    main()