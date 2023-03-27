"""
Counts the number of add instructions in a json bril program read from stdin
"""
import json
import sys


def count_adds(program):
    """
    Counts the number of add instructions in a program.

    Parameters:
        program The program to count the add instructions in.

    Returns:
        The number of add instructions in program
    """
    add_count = 0
    for function in program["functions"]:
        for inst in function["instrs"]:
            if inst["op"] == "add":
                add_count = add_count + 1

    return add_count


if __name__ == "__main__":
    program = json.load(sys.stdin)
    add_count = count_adds(program)
    print(f"{add_count} add instructions")
