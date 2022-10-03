from math import pi
from unittest import result


def calculate_sum(n):
    '''
    This function should calculate the sum every number from 0 up until n (NON-INCLUSIVE).

    @return: this method should just return the sum of every number from 0 to n.
    '''
    result = 0

    for i in range (0, n):
        result=result+i

    return result  


def calculate_pi(n):
    '''
    This function calculates Pi using Leibniz's formula. The formula is calculated as
    the following:

        X = 1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + 4/13 - ...
    Notice the pattern within the formula. Please note that this series is never-ending
    and the higher value you pass in for n the closer the value of X converges to the value
    of Pi.

    Hint: 
        1. init your denominator k outside your loop.
        2. run a loop from 0 to n
        3. use mod inside the loop to determine whether to add or subtract 4/k
        4. increment k by 2
        5. repeat from step 2 until you reach end of range.

    @arg(n): the number of terms in the series to calculate (must be odd) (INCLUSIVE).
    @return: the calculated
    '''


    result = 0


    # your logic
    k = 1
    for i in range(n):
        if i % 2 == 0:
            result = result + 4/k 
        else:
            result = result - 4/k 

        #increment denom by 2
        k = k + 2      

    return result


def fibonacci(n):
    '''
    The fibonacci sequence is a series of numbers. The next number is found
    by adding up the two numbers before it in the sequence. The series looks
    like this [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...]

    Hint: the first two numbers are 0 and 1. 

    @arg(n): the number of terms in the series to calculate.
    @return: the sum of the fibonacci numbers up until n.
    '''

    result = 0
    i = 0
    first = 0 
    second = 1

    if n <= 0:
        return 0

    elif n == 1:
        return first

    #else...        
    for i in range(0, n):
        result = first = second
        first = second
        second = result

        #increment i
        i += i

    # your logic

    return result