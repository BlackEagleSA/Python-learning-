# @Author: Turki Alrifaie
# @Date:   2018-11-29T14:58:46-05:00
# @Email:  alrifaie.t@husky.neu.edu
# @Filename: basic.py
# @Last modified by:   Turki Alrifaie
# @Last modified time: 2018-11-29T15:46:25-05:00


"""

After doing some reading on wikipedia, I decided to work with the Quadratic sieve algorithm (https://en.wikipedia.org/wiki/Quadratic_sieve)

"""
import math


def findRoot(num):
    x = math.ceil(math.sqrt(num))

def generateList(root, num):
    flag = 1
    counter = 1
    list = []

    while (flag):
         list.append((root ** 2) % num)
         root +=1
         counter +=1
         if counter == 5:
             flag = 0

def findSquare(list, num):
    flag = 0
    temp = temp + list
    max = len(temp)
    base, var = 0

    """while(!flag):
        for i in range(max):
            temp =""" 




def solver(num):
    root = findRoot(num)
    list = generateList(root, num)
    square = findSquare(list, num)



if __name__ == "__main__":
