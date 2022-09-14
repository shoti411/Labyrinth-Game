import json

# acceptable_string_map :
#   (Dict<String, Dict<String, String>>) Maps string inputs into corresponding acceptable strings
acceptable_string_map = {
    "UP": {"LEFT": "┘", "RIGHT": "└"},
    "DOWN": {"LEFT": "┐", "RIGHT": "┌"}
}

def filter_input(input_str: str) -> list:
    """
    :param: input_str (str): input_str that is filled with json objects.
    :return: (list<str>) filtered input_str

    Takes in a string of JSON objects. Filters out all whitespace from the string and breaks it up by JSON object into a list.
    Returns that list.
    """
    return input_str.replace(' ','').replace('}','}*').split('*')[:-1]

def xjson() -> int:
    """
    :param: None
    :return: (int) exit code

    Takes stream of well-formed JSON strings from STDIN, parses and then prints JSON array of corresponding acceptable
    strings. Returns an exit code.
    """

    # To start we will grab all inputs from user.
    input_line = ''
    while True:
        try:
            input_line += input()
        # ending successfully (on user-break with 'CTRL-D') or End of File
        except EOFError:
            break

    # Filter input and convert to list
    input_strs = filter_input(input_line)

    # Convert list to json array
    return_array = []
    for input_str in input_strs:
        input_json = json.loads(input_str)
        next_string = acceptable_string_map[input_json['vertical']][input_json['horizontal']]
        return_array.append(next_string)
    print(json.dumps(return_array, ensure_ascii=False), end='')

    return 0


if __name__ == "__main__":
    xjson()
