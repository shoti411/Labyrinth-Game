# acceptable_strings : (List-of String) -> the only valid String inputs for the program
acceptable_strings = ["┘", "┐", "└", "┌"]

# unacceptable_output : (String) -> the output String when invalid String is taken as input
unacceptable_output = 'unacceptable input'


def acceptable(input_str):
    return input_str in acceptable_strings


def unacceptable():
    print(unacceptable_output)
    exit(1)


def main():
    return_str = ''
    while True:
        try:
            input_str = eval(input())
            if acceptable(input_str):
                return_str += input_str
            else:
                unacceptable()

        # ending successfully (on user-break with 'CTRL-D')
        except SyntaxError:
            print(return_str)
            return 0


if __name__ == "__main__":
    main()
