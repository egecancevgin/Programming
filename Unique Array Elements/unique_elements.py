def unique_arr_elements(array):
    """
    Finds and returns the unique elements of the array with a list.
    :param array: Input array to check
    :return: Output array of unique elements
    Complexity: ~O(n^2), ~O(n*k) where n is the number of elements in the array
    """

    # Initialize the list of unique_values
    unique_values = []

    # Traverse the whole array for checking the unique values
    for element in array:
        if element not in unique_values:
            unique_values.append(element)

    return unique_values


def unique_arr_elm_presort(array):
    """
    Finds and returns the unique elements of the array with a list
    by using presorting and binary search approaches.
    :param array: Input array to check
    :return: Output array of unique elements
    Complexity: O(n*logn), S(n)
    """

    # Create a sorted copy of input array
    temp_arr = sorted(array)

    # Create a list to store unique elements
    unique_values = []

    # Iterate over the sorted array and add unique elements to the list
    for element in temp_arr:
        if binary_search(unique_values, element) == -1:
            unique_values.append(element)

    return unique_values


def binary_search(array, key):
    """
    Returns the index of the wanted element in an array iteratively
    :param array: Input array to search on
    :param key: The integer or float key to look for
    :return: Index as an integer of the wanted element
    Complexity: O(n*logn), S(n^2)
    """
    if len(array) == 0:
        return -1

    # Initialize indices to search for key
    min = 0
    max = len(array) - 1

    # Iterate until the search range is empty
    while min <= max:
        # Calculate the middle index of the search range
        mid = (min + max) // 2

        # If the middle element is less than the key, search the right half of the range
        if array[mid] < key:
            min = mid + 1

        # If the middle element is greater than the key, search the left half of the range
        elif array[mid] > key:
            max = mid - 1

        # If the middle element is greater than the key, search the left half of the range
        else:
            return mid

    # Key not found, return -1
    return -1


def main():
    """Driver Function"""
    array = [5, 3, 2, 8, 6, 3, 5, 1, 2, 8, 1]

    print("Unique elements of the {} array are: {}\n".format(array, unique_arr_elements(array)))

    print("Unique elements of the {} array by presorting are: {}\n".format(array, unique_arr_elm_presort(array)))


if __name__ == '__main__':
    main()
