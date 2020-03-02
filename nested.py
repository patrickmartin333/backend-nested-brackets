#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "patrickmartin333, with a TON of help from Piero and the demo!"

import sys

# Begin with opening/closing brackets paired up via their indexes
opening_brackets = ["(*", "(", "[", "{", "<"]
closing_brackets = [")*", ")", "]", "}", ">"]


def is_nested(line):
    """Validate a single input line for correct nesting"""
    stack = []  # initial empty stack
    token_counter = 0
    while line:  # while line exists (loop through each line until false..)  We are only looking at the tokens defined above in opening/closing brackets list
        # token being the bracket within the line.  Want to figure out token each time through loop
        token = line[0]

        token_counter += 1
        line = line[(len(token)):]

        if token in opening_brackets:
            stack.append(token)
        elif token in closing_brackets:
            closing_index = closing_brackets.index(token)
            expected_opener = opening_brackets[closing_index]
            if stack.pop() != expected_opener:
                return "NO" + str(token_counter)

    # After loop has finished, check if there is anythng in stack
    # if stack is not empty..
    if stack:
        return "NO " + str(token_counter)

    else:
        return "YES"


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file
    with open(args[0]) as input_file:
        with open('output.txt', 'w') as output_file:  # creating text file containing output
            for line in input_file:
                # passing each line in file provided as command-line argument(args[0])
                result_string = is_nested(line)
                print(result_string)
                output_file.write(result_string + "\n")


if __name__ == '__main__':
    main(sys.argv[1:])
