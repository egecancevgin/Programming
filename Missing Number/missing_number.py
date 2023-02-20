

def missing_number(arr):
    """
    Detects the missing number of an array, the array should have one missing number at all
    :param arr: The input array, without redundant values
    :return: The missing integer
    Complexity: O(n*logn), S(n)
    """

    # Copy and sort the array
    temp_arr = arr.copy()
    temp_arr.sort()

    # Check the next element of each element
    for i in range(len(temp_arr)):
        if temp_arr[i] + 1 != temp_arr[i+1]:
            return temp_arr[i] + 1

    return -1


def main():
    """ Driver function."""

    test_arr = [5, 9, 4, 2, 3, 1, 10, 8, 7]

    print("The missing number of the {} is: {}".format(test_arr, missing_number(test_arr)))


if __name__ == '__main__':
    main()

