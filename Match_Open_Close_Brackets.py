""" matched function is use to determine open"(" and close ")" brackets.
if it matches return true,else return as false"""


def matched(input_string):

    open_bracket_count = []
    balanced = True
    index = 0
    while index < len(input_string) and balanced:
        token = input_string[index]
        if token == "(":
            open_bracket_count.append(token)

        elif token == ")":

            if len(open_bracket_count) == 0:  # There is no matching open brackets, hence return false
                balanced = False
            else:
               open_bracket_count.pop()    # There is matching open brackets, hence pop the element from the list.
        index += 1
    return balanced and len(open_bracket_count) == 0

print(matched("(7)(a"))