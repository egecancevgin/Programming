

def first_duplicate(arr):
    """
    Returns the first duplicate number of the given array with the given order
    :param arr: Input array
    :return: The first duplicate value or Null if there are no duplicates
    Complexity: O(n), S(n)
    """
    # Initialize the symbol table
    element_dict = dict()

    # Fill the symbol table with zeros
    for element in arr:
        element_dict[element] = 0

    # Increase the frequencies and if it surpasses one, return that number
    for element in arr:
        element_dict[element] += 1
        if element_dict[element] > 1:
            return element

    return None


def main():
    """ Driver function."""

    test_arr = [15, 12, 11, 16, 12, 18, 15, 11, 19, 20]

    print("First duplicate value of the {} array is: {}.".format(test_arr, first_duplicate(test_arr)))


if __name__ == '__main__':
    main()
