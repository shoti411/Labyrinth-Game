import json

# acceptable_string_map :
#   (Dict<String, Dict<String, String>>) Maps string inputs into corresponding acceptable strings
acceptable_string_map = {
    "UP": {"LEFT": "┘", "RIGHT": "└"},
    "DOWN": {"LEFT": "┐", "RIGHT": "┌"}
}


def xjson() -> int:
    """
    :param: None
    :return: (int) exit code

    Takes stream of well-formed JSON strings from STDIN, parses and then prints JSON array of corresponding acceptable
    strings. Returns an exit code.
    """
    return_array = []
    while True:
        try:
            input_json = json.loads(input())
            next_string = acceptable_string_map[input_json['vertical']][input_json['horizontal']]
            return_array.append(next_string)
        # ending successfully (on user-break with 'CTRL-D')
        except EOFError:
            print(json.dumps(return_array, ensure_ascii=False))
            return 0

    return 1


if __name__ == "__main__":
    xjson()
