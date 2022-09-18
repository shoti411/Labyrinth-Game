import json


def xgui():
    input_line = ''
    while True:
        try:
            input_line += input()
        # ending successfully (on user-break with 'CTRL-D') or End of File
        except EOFError:
            break


if __name__ == "__main__":
    xgui()
