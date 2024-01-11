# @Author: Turki A Alrifaie
# @Date:   2018-12-05T10:04:08-05:00
# @Email:  alrifaie.t@husky.neu.edu
# @Filename: basic.py
# @Last modified by:   Turki A Alrifaie
# @Last modified time: 2018-12-05T10:59:28-05:00
# @License: Free

"""

Problem Description
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""
from math import *


def power():
    global ans, sum, large

    large = 0.0
    sum = 0.0
    a =0.0

    for a in (1,100):
        sum =0.0
        for b in range (1,100):
            #print("intital a: "+str(a))
            #print("intital b: "+str(b))
            digit= pow(a,b)
            #print("intital digit: "+str(digit))
            while (digit != 0):
                sum = sum + (digit % 10)
                #print ("the sum is: " + str(sum))
                digit = digit//10
                #print("After disect: " + str(digit))
            if (large < sum):
                large = sum
            sum =0.0
            #print("Large=" + str(large))
    print("Large=" + str(large))

if __name__ == "__main__":
    power()
    print()
