

def is_palindrome(number):
    """
    Checks the number if it is in palindrome format (121, 12321, ...)
    :param number: Input integer
    :return: The corresponding boolean value
    Complexity: O(n), S(n)
    """

    num_list = []
    temp_num = number

    while True:
        # Access to the last digit of the number
        a = temp_num % 10

        # Add the digit into the numbers list, FIFO way
        num_list.insert(0, a)

        # Go to the next digit of the number
        temp_num = temp_num // 10
        if temp_num == 0:
            break

    for i in range(len(num_list)):
        # print(num_list[i], num_list[len(num_list) - 1 - i], i, len(num_list) - 1 - i)
        if num_list[i] != num_list[len(num_list) - 1 - i]:
            return False

    return True


def main():
    """ Driver function."""

    # Initialize the numbers
    number_I = 53223
    number_II = 312353213

    print("Is {} number palindrome: {}".format(number_I, is_palindrome(number_I)))

    print("Is {} number palindrome: {}".format(number_II, is_palindrome(number_II)))


if __name__ == '__main__':
    main()
