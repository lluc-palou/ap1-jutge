def difference(v1: list[float], v2: list[float]) -> list[float]:
    """Given two sorted lists returns another sorted list with the
    elements of the difference from both, without repetitions."""

    v: list[float] = []
    n1, n2 = len(v1), len(v2)
    i1, i2 = 0, 0
    last_v2_element = 0.0
    last_v_element = 0.0

    while i1 < n1 and i2 < n2:
        if v1[i1] == v2[i2]:
            last_v2_element = v2[i2]
            i1 += 1
            i2 += 1

        elif v1[i1] < v2[i2] and last_v2_element != v1[i1] and last_v_element != v1[i1]:
            v.append(v1[i1])
            last_v_element = v1[i1]
            
            i1 += 1

        elif v1[i1] < v2[i2] and last_v2_element == v1[i1]:
            i1 += 1
        
        else:
            i2 += 1
    
    while i1 < n1:
        if v1[i1] != last_v2_element and last_v_element != v1[i1]:
            v.append(v1[i1])
            last_v_element = v1[i1]
            i1 += 1
            
        else:
            i1 += 1

    return v

def main() -> None:
    v1 = [9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.7, 9.8, 9.9]
    v2 = [0.0]
    v = difference(v1, v2)
    print(v)

if __name__ == '__main__':
    main()