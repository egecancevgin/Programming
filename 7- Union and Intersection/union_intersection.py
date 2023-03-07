

def union_intersection(arr_1, arr_2):
    """
    Applies union and intersection operations to two input arrays, uses set data structure
    :param arr_1: First input array
    :param arr_2: Second input array
    :return: union and intersection sets
    Complexity: O(n^2), S(n)
    """
    union = set()
    intersection = set()

    # Traverse the first array and also detect the common elements
    for element in arr_1:
        union.add(element)
        if element in arr_2:
            intersection.add(element)

    for element in arr_2:
        union.add(element)

    return union, intersection


def main():
    """ Driver function."""

    array_1 = [1, 5, 3, 6, 0, 8]
    array_2 = [2, 5, 4, 7, 8, 9]

    print(union_intersection(array_1, array_2))


if __name__ == '__main__':
    main()
