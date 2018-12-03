# @Author: Turki A Alrifaie
# @Date:   2018-12-03T13:51:43-05:00
# @Email:  alrifaie.t@husky.neu.edu
# @Filename: basic.py
# @Last modified by:   Turki A Alrifaie
# @Last modified time: 2018-12-03T14:16:49-05:00
# @License: Free


def sumofSquares(range_):
    global totalofSquares, ans

    totalofSquares = 0

    for i in range(1, range_+1):
        totalofSquares = totalofSquares + i ** 2

def squareofSum(range_):
    global ans, totalsquareSums
    totalsquareSums = 0
    temp = 0
    for i in range(1, range_+1):
        temp = temp + i

    totalsquareSums = temp ** 2



def run():
    global ans, totalsquareSums, totalofSquares
    sumofSquares(100)
    squareofSum(100)

    ans = totalsquareSums - totalofSquares


if __name__ == "__main__":
    run()
    print("difference is {0}".format(ans))
