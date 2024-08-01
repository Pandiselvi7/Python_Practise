"""checkPrime function will determine whether the number is prime or not.
first  the number will divide by 2 if the output is 0 ,return false. else it will continue in the loop"""


def checkprime(num, iter=2):
    if num == iter:
        return True
    if num % iter == 0:
        return False
    if num < 2:
        return False
    return checkprime(num, iter + 1)


'''sumprime function is will take input as list. Findout prime numbers in the list then sum those numbers.
 It will take non-negative and negattive numbers as input'''


def sumprimes(lis):
    global sum
    sum = 0
    for num in lis:
        if checkprime(num):
            sum = sum + num
    return sum


print(sumprimes([3, 3, 1, 13]))