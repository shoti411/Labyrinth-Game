###############################################################################################

# acceptable_strings : (List-of String) -> the only valid String inputs for the program
acceptable_strings = ["┘", "┐", "└", "┌"]
# unacceptable_output : (String) -> the output String when invalid String is taken as input
unacceptable_output = 'unacceptable input'

###############################################################################################


def acceptable(input_str: str) -> bool:
    """
    Parameters:
    input_str: given string

    Returns boolean

    acceptable represents a function to check if a given string is a acceptable string.
    """

    return input_str in acceptable_strings


def xcollects() -> int:
    """
    Parameters: None

    Returns exit code

    xcollects reads a stream of lines from STDIN and prints a single string on a line by itself to STDOUT of all the valid STDIN characters.
    Acceptable strings are one of: "┘", "┐", "└", "┌" and includes the quotes. 
    If any input is not acceptable the program prints "unacceptable input" also on a line by itself.
    """

    return_str = ''
    while True:
        try:
            input_str = eval(input())
            if acceptable(input_str):
                return_str += input_str
            else:
                print(unacceptable_output)
                exit(1)
        # ending successfully (on user-break with 'CTRL-D')
        except SyntaxError:
            print(return_str)
            return 0
        # input is not surrounded in quotes therefore unacceptable
        except NameError:
            print(unacceptable_output)
            exit(1)


if __name__ == "__main__":
    xcollects()
