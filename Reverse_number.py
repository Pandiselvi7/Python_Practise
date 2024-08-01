"""intreverse function is used to reverse the numbbers"""


def intreverse(number):
    rev_num = str(number)  # cast into string
    return rev_num[::-1]


print(intreverse(242789))