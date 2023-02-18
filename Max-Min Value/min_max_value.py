import numpy as np


def minimum(arr):
    """
    Finds the minimum of an array and returns it
    :param arr: Input integer or floating point array
    :return: The minimum value
    Complexity: ~O(n), S(1)
    """

    # Initialize the maximum number possible
    min_value = 999999999

    # Traverse the whole array and check if there are smaller elements
    for element in arr:
        if element < min_value:
            min_value = element
    return min_value


def maximum(arr):
    """
    Finds the maximum of an array and returns it
    :param arr: Input integer or floating point array
    :return: The maximum value
    Complexity: ~O(n), S(1)
    """

    # Initialize the minimum number possible
    max_value = -999999999

    # Traverse the whole array and check if there are any bigger elements
    for element in arr:
        if element > max_value:
            max_value = element

    return max_value


def main():
    """ Driver function."""

    # Initializing the testing array
    test_arr = [32.4, 21.7, 174.9, 18.3, 46.2, 68.1, 98.6, 13.4, 23.5, 108.4]

    # Calling and printing the minimum() function
    print("The minimum value of {} array is {}.\n".format(test_arr, minimum(test_arr)))

    # Calling and printing the maximum() function
    print("The maximum value of {} array is {}.\n".format(test_arr, maximum(test_arr)))


if __name__ == '__main__':
    main()
