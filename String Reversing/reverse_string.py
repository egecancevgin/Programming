

def reverse_string(string):
    """
    Returns the reversed version of the argument string
    :param string: A normal string
    :return: rev_string
    Complexity: O(n), S(n).
    """

    temp_list = []
    rev_string = ""

    for chars in string:
        temp_list.insert(0, chars)

    for chars in temp_list:
        print(chars)
        rev_string += chars

    return rev_string


def main():
    """Driver function."""

    # Initialize the test string
    test_string = "Egecan"

    print("The reversed version of the string {} is: {}.".format(test_string, reverse_string(test_string)))


if __name__ == '__main__':
    main()
