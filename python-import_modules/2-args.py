#!/usr/bin/python3
if __name__ ==" __main__":
    import sys

    if len(argv) == 1:
        print("number of argument(s):.")
    else:
        print(f"number of arguments(s): {len(argv) - 1}{'.' if len(argv) == 2 else ':'}")

        for i, arg in enumerate(argv[1:], 1):

            print(f"{i}: {argv}")
